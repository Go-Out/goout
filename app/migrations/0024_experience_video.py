# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20160419_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='video',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
