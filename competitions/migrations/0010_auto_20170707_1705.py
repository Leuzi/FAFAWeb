# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0009_auto_20170707_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='Type',
        ),
        migrations.AddField(
            model_name='edition',
            name='Active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='edition',
            name='Competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.CompetitionType'),
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
    ]
