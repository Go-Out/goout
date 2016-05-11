# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import timedelta


# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def __unicode__(self):
    return self.name

class Experience(models.Model):
  image_paths = (
    ("Amigo", "Amigo"),
    ("Bici+Tequila", "Bici Tequila"),
    ("Camino+Mágico+Tequila", "Camino Mágico Tequila"),
    ("Cuatrimoto+hasta+la+piedra+bola", "Cuatrimoto hasta la piedra bola"),
    ("Familia", "Familia"),
    ("Nevado+de+Colima", "Nevado de Colima"),
    ("Pareja+Adrenalina", "Pareja Adrenalina"),
    ("Relajación", "Relajación"),
    ("Tarzán", "Tarzán"),
    ("Tirolesa", "Tirolesa"),
    ("default", "default"),
  )

  name = models.CharField(max_length=50)
  active = models.BooleanField(default=True)
  subheader = models.CharField(max_length=250, blank=True)
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
  images_path = models.CharField(default="default", choices=image_paths, max_length=100)
  video = models.CharField(blank=True, max_length=1000)
  categories = models.ManyToManyField(Category)
  experiences = models.ManyToManyField("self", blank=True)

  def __str__(self):
    return self.name

  def __unicode__(self):
    return self.name

class Code(models.Model):
  code = models.CharField(max_length=6)
  available = models.BooleanField(default=True, editable=False)

  def __str__(self):
    return self.code

  def __unicode__(self):
    return self.code
