from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Experience(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  location = models.CharField(max_length=250)
  availability = models.TextField(blank=True, help_text="Each day in a new line")
  duration = models.DurationField(blank=True, help_text="Number of hours")
  description = models.TextField(blank=True, help_text="Each paragraph in a new line")
  itinerary = models.TextField(blank=True, help_text="Each paragraph in a new line")
  included = models.TextField(blank=True, help_text="Each one in a new line")
  requirements = models.TextField(blank=True, help_text="Each one in a new line")
  gear = models.TextField(blank=True, help_text="Each one in a new line")
  additional = models.TextField(blank=True, help_text="Each one in a new line")
  images = models.TextField(blank=True, editable=False)
  categories = models.ManyToManyField(Category)

  def __str__(self):
    return self.name
