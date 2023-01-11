# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.1 on 2020-10-19 12:16

from django.db import migrations


def alter_role(apps, schema_editor):
    if schema_editor.connection.vendor != "postgresql":
        return

    settings = schema_editor.connection.settings_dict

    template = "ALTER ROLE {} SET {{}} = {{}}".format(
        schema_editor.quote_name(settings.get("ALTER_ROLE", settings["USER"]))
    )

    schema_editor.execute(template.format("timezone", "UTC"))


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(
            alter_role, migrations.RunPython.noop, elidable=False, atomic=False
        )
    ]
