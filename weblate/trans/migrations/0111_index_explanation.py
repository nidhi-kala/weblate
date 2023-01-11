# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.4 on 2021-01-27 07:15

from django.db import migrations

from weblate.utils.db import MY_DROP, MY_FTX, PG_DROP, PG_TRGM


def create_index(apps, schema_editor):
    vendor = schema_editor.connection.vendor
    if vendor == "postgresql":
        # Create GIN trigram index on searched fields
        schema_editor.execute(PG_TRGM.format("unit", "explanation", ""))
    elif vendor == "mysql":
        schema_editor.execute(MY_FTX.format("unit", "explanation"))
    else:
        raise Exception(f"Unsupported database: {vendor}")


def drop_index(apps, schema_editor):
    vendor = schema_editor.connection.vendor
    if vendor == "postgresql":
        schema_editor.execute(PG_DROP.format("unit", "explanation"))
    elif vendor == "mysql":
        schema_editor.execute(MY_DROP.format("unit", "explanation"))
    else:
        raise Exception(f"Unsupported database: {vendor}")


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0110_auto_20210120_0845"),
    ]

    operations = [
        migrations.RunPython(
            code=create_index,
            reverse_code=drop_index,
            atomic=False,
        ),
    ]
