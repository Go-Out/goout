from __future__ import unicode_literals

from django.db import models
from datetime import timedelta


IMAGES_FOLDER = "app/static/app/images/experiences/"

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def __unicode__(self):
    return self.name

class Experience(models.Model):
  name = models.CharField(max_length=50)
  active = models.BooleanField(default=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  people = models.IntegerField(default=1)
  location = models.CharField(max_length=250)
  availability = models.TextField(blank=True, help_text="Each day in a new line")
  duration = models.DurationField(default=timedelta(), help_text="Number of hours")
  description = models.TextField(blank=True, help_text="Each paragraph in a new line")
  itinerary = models.TextField(blank=True, help_text="Each paragraph in a new line")
  included = models.TextField(blank=True, help_text="Each one in a new line")
  requirements = models.TextField(blank=True, help_text="Each one in a new line")
  gear = models.TextField(blank=True, help_text="Each one in a new line")
  additional = models.TextField(blank=True, help_text="Each one in a new line")
  images_path = models.FilePathField(path=IMAGES_FOLDER, allow_folders=True, allow_files=False, default=IMAGES_FOLDER + "default")
  video = models.CharField(blank=True, max_length=1000)
  categories = models.ManyToManyField(Category)
  experiences = models.ManyToManyField("self", blank=True)

  def __str__(self):
    return self.name

  def __unicode__(self):
    return self.name
