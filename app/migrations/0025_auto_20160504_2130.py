# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 21:30
from __future__ import unicode_literals

from django.db import migrations


CODES_FILE = "app/migrations/data/codes.csv"

def insert_codes(apps, schema_editor):
  codes = read_lines_from_file(CODES_FILE)

def read_lines_from_file(file_name):
  with open(file_name) as f:
    return f.readlines()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_experience_video'),
    ]

    operations = [
    ]
