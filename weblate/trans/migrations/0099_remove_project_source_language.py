# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-09-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0098_move_source_language"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="source_language",
        ),
    ]
