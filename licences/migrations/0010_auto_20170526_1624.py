# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0009_auto_20170526_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenceduration',
            name='MaximunBirthDate',
            field=models.DateField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='licenceduration',
            name='MinimumBirthDate',
            field=models.DateField(blank=True, default=None),
            preserve_default=False,
        ),
    ]
