# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-01 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160224_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='images',
            field=models.TextField(blank=True, editable=False),
        ),
    ]