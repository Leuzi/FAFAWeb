# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_auto_20170602_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitionconditions',
            name='Years',
        ),
        migrations.AddField(
            model_name='competitionconditions',
            name='Gender',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Open')], default='O', max_length=1),
        ),
    ]
