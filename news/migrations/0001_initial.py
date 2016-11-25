# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-20 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header', models.CharField(max_length=25)),
                ('SubHeader', models.CharField(max_length=50)),
                ('Body', models.CharField(max_length=5000)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Likes', models.PositiveSmallIntegerField(default=0)),
                ('Facebook', models.PositiveSmallIntegerField(default=0)),
                ('Pinterest', models.PositiveSmallIntegerField(default=0)),
                ('GooglePlus', models.PositiveSmallIntegerField(default=0)),
                ('Slug', models.SlugField()),
            ],
            options={
                'ordering': ['Date'],
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='new',
            name='Template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Template'),
        ),
    ]