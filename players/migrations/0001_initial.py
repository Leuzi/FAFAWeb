# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LicenceId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LicenceId', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=12)),
                ('Name', models.CharField(max_length=50)),
                ('Surname', models.CharField(max_length=50)),
                ('BirthDate', models.DateField()),
                ('Country', django_countries.fields.CountryField(max_length=2)),
                ('ZIPCode', models.CharField(max_length=7)),
                ('City', models.CharField(max_length=20)),
                ('Region', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Mail', models.EmailField(max_length=254)),
                ('Photo', models.ImageField(upload_to=b'.')),
            ],
        ),
        migrations.AddField(
            model_name='licenceid',
            name='Player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player'),
        ),
    ]