# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160126_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='availability',
            field=models.TextField(blank=True, help_text='Each date in a new line (yyyy-mm-dd)'),
        ),
    ]