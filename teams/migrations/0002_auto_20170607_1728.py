# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Logo',
            field=models.ImageField(default=b'images/default.png', upload_to=b'files/thumbs/'),
        ),
    ]
