# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0005_auto_20170526_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenceduration',
            name='MaximunBirthDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='licenceduration',
            name='MinimumBirthDate',
            field=models.DateField(blank=True),
        ),
    ]
