# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0004_auto_20170519_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenceduration',
            name='MaximunBirthDate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='licenceduration',
            name='MinimumBirthDate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]