# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-20 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20161120_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='Season',
        ),
        migrations.RemoveField(
            model_name='field',
            name='Season',
        ),
    ]