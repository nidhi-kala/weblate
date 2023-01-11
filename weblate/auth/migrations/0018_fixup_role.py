# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2.4 on 2021-09-27 11:49

from django.db import migrations
from django.db.models import Count


def fixup_role(apps, schema_editor):
    Role = apps.get_model("weblate_auth", "Role")
    db_alias = schema_editor.connection.alias
    duplicates = (
        Role.objects.using(db_alias)
        .values("name")
        .annotate(count=Count("id"))
        .filter(count__gt=1)
    )
    for duplicate in duplicates:
        roles = Role.objects.using(db_alias).filter(name=duplicate["name"])
        toremove = []
        keep = None
        for role in roles:
            if role.group_set.count() == 0:
                toremove.append(role)
            elif keep is None:
                keep = role
        if keep is None:
            keep = toremove.pop()
        for role in roles:
            if role in toremove:
                keep.group_set.add(*role.group_set.all())
                print(f"Removing duplicate role {role.name}")
                role.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("weblate_auth", "0017_alter_user_email"),
    ]

    operations = [
        migrations.RunPython(
            fixup_role, migrations.RunPython.noop, elidable=False, atomic=False
        )
    ]
