# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_experience_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
