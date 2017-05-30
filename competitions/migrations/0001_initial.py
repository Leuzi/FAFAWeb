# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0002_auto_20170519_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('MinimumBirthDate', models.DateField()),
                ('MaximumBirthDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=12)),
                ('Region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regions.Region')),
            ],
        ),
    ]