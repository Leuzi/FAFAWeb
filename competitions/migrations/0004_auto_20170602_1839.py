# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20170519_1739'),
        ('competitions', '0003_auto_20170526_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='Teams',
            field=models.ManyToManyField(to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='Active',
            field=models.BooleanField(default=False),
        ),
    ]
