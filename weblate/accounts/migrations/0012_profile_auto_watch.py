# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.4 on 2021-02-08 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_auto_20210106_1903"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="auto_watch",
            field=models.BooleanField(
                default=settings.DEFAULT_AUTO_WATCH,
                help_text="Whenever you translate a string in a project, you will start watching it.",
                verbose_name="Automatically watch projects on contribution",
            ),
        ),
    ]
