# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-09-15 10:30

from django.db import migrations
from django.db.models import F


def update_source_unit(apps, schema_editor):
    Unit = apps.get_model("trans", "Unit")
    Project = apps.get_model("trans", "Project")
    db_alias = schema_editor.connection.alias

    source_units = Unit.objects.using(db_alias).filter(
        translation__language=F("translation__component__source_language")
    )
    total = source_units.count()
    processed = 0

    for project in Project.objects.using(db_alias).iterator():
        has_labels = project.label_set.exists()
        for source in source_units.filter(
            translation__component__project=project
        ).iterator():
            processed += 1

            if processed % 1000 == 0:
                percent = int(100 * processed / total)
                print(f"Updating source units {percent}% [{processed}/{total}]...")
            # Filter matching translation units
            translations = (
                Unit.objects.using(db_alias)
                .filter(
                    translation__component=source.translation.component,
                    id_hash=source.id_hash,
                )
                .exclude(pk=source.pk)
            )
            # Update source_unit attribute and wipe extra_flags and explanation
            update = {"source_unit": source}
            if source.extra_flags:
                update["extra_flags"] = ""
            if source.explanation:
                update["explanation"] = ""
            translations.update(**update)
            # Wipe labels link to translations
            if has_labels and source.labels.exists():
                Unit.labels.through.objects.using(db_alias).filter(
                    unit__in=translations
                ).delete()

    if total:
        print(f"Updating source units completed [{processed}/{total}]")


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0102_unit_source_unit"),
    ]

    operations = [migrations.RunPython(update_source_unit, elidable=True)]
