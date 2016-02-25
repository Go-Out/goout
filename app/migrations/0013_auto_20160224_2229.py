# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-24 22:18
from __future__ import unicode_literals
from django.db import migrations
from datetime import timedelta
from django.core.exceptions import ObjectDoesNotExist
from .. utils import text_as_json


EXPERIENCES_FILE = "app/migrations/data/experiences_es.tsv"
NEW_LINE_DELIMITER = "|"

def insert_experiences(apps, schema_editor):
  experience_lines = read_lines_from_file(EXPERIENCES_FILE)[1:]

  Experience = apps.get_model("app", "Experience")
  Category = apps.get_model("app", "Category")

  for line in experience_lines:
    fields = line.decode('utf8').rstrip().split("\t")

    if int(fields[12]):
      try:
        category = Category.objects.get(name=fields[9])
      except ObjectDoesNotExist:
        category = Category(name=fields[9])
        category.save()

      experience = Experience(
          name=fields[0],
          price=float(fields[1]),
          description=text_as_json(fields[2], NEW_LINE_DELIMITER),
          location=fields[3],
          availability=text_as_json(fields[4], NEW_LINE_DELIMITER),
          duration=timedelta(hours=float(fields[5])),
          requirements=text_as_json(fields[6], NEW_LINE_DELIMITER),
          included=text_as_json(fields[7], NEW_LINE_DELIMITER),
          additional=text_as_json(fields[8], NEW_LINE_DELIMITER),
          itinerary=text_as_json(fields[10], NEW_LINE_DELIMITER),
          gear=text_as_json(fields[11], NEW_LINE_DELIMITER)
      )
      experience.save()
      experience.categories.add(category)

def delete_experiences(apps, schema_editor):
  Experience = apps.get_model("app", "Experience")
  Experience.objects.all().delete()

def read_lines_from_file(file_name):
  with open(file_name) as f:
    return f.readlines()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160224_2228'),
    ]

    operations = [
        migrations.RunPython(insert_experiences, delete_experiences),
    ]