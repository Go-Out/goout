from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Experience(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.TextField()
  location = models.CharField(max_length=100)
  availability = models.CharField(max_length=100)
  duration = models.DurationField(blank=True)
  participants = models.IntegerField(default=1)
  requirements = models.TextField(default="[]")
  included = models.TextField(default="[]")
  additional = models.TextField(blank=True)
