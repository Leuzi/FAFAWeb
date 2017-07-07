# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0007_auto_20170707_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionconditions',
            name='EndDate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='competitionconditions',
            name='MaximumBirthDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]