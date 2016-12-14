# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-09 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logoseason',
            name='Season',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='seasons.Season'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logoseason',
            name='Team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='logo_of', to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uniformseason',
            name='Season',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='seasons.Season'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uniformseason',
            name='Team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_of', to='teams.Team'),
            preserve_default=False,
        ),
    ]