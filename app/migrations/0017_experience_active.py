# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-29 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20160319_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
