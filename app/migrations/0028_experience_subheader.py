# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-10 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20160504_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='subheader',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
