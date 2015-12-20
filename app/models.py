from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Demographic(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Experience(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.TextField()
  location = models.CharField(max_length=100)
  availability = models.CharField(max_length=100)
  duration = models.DurationField(blank=True, help_text="Number of hours")
  participants = models.IntegerField(default=1)
  requirements = models.TextField(help_text="Each one in a new line")
  included = models.TextField(help_text="Each one in a new line")
  additional = models.TextField(help_text="Each one in a new line")
  categories = models.ManyToManyField(Category)
  demographics = models.ManyToManyField(Demographic)

  def __str__(self):
    return self.name
