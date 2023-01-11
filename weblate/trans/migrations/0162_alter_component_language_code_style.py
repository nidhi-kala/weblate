# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.3 on 2022-12-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0161_alter_project_name_alter_project_web"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="language_code_style",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Default based on the file format"),
                    ("posix", "POSIX style using underscore as a separator"),
                    ("bcp", "BCP style using hyphen as a separator"),
                    (
                        "posix_long",
                        "POSIX style using underscore as a separator, including country code",
                    ),
                    (
                        "bcp_long",
                        "BCP style using hyphen as a separator, including country code",
                    ),
                    (
                        "bcp_legacy",
                        "BCP style using hyphen as a separator, legacy language codes",
                    ),
                    ("bcp_lower", "BCP style using hyphen as a separator, lower cased"),
                    ("android", "Android style"),
                    ("appstore", "Apple App Store metadata style"),
                    ("googleplay", "Google Play metadata style"),
                    ("linux", "Linux style"),
                ],
                default="",
                help_text="Customize language code used to generate the filename for translations created by Weblate.",
                max_length=20,
                verbose_name="Language code style",
            ),
        ),
    ]
