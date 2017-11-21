# -*- coding: utf-8 -*-
# Generated by Django 1.11.5.dev20170816164241 on 2017-11-21 10:36
from __future__ import unicode_literals

from django.db import migrations


def migrate_state(apps, schema_editor):
    Unit = apps.get_model('trans', 'Unit')

    Unit.objects.filter(translated=True).update(state=20)
    Unit.objects.filter(approved=True).update(state=30)
    Unit.objects.filter(fuzzy=True).update(state=10)


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0106_unit_state'),
    ]

    operations = [
        migrations.RunPython(migrate_state),
    ]
