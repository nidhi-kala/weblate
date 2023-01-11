# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2 on 2021-05-12 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0009_alter_metric_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="metric",
            options={"verbose_name": "Metric", "verbose_name_plural": "Metrics"},
        ),
    ]
