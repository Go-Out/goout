from django.contrib import admin
from .models import Experience, Category
from datetime import timedelta
from django import forms
from .utils import text_as_json, json_as_text

# Register your models here.

class ExperienceForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(ExperienceForm, self).__init__(*args, **kwargs)
    if self.instance.duration is not None:
      self.initial['availability'] = json_as_text(self.instance.availability)
      self.initial['duration'] = self.instance.duration.seconds / 3600
      self.initial['description'] = json_as_text(self.instance.description)
      self.initial['itinerary'] = json_as_text(self.instance.itinerary)
      self.initial['included'] = json_as_text(self.instance.included)
      self.initial['requirements'] = json_as_text(self.instance.requirements)
      self.initial['gear'] = json_as_text(self.instance.gear)
      self.initial['additional'] = json_as_text(self.instance.additional)

class ExperienceAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'location', 'active')
  form = ExperienceForm

  def save_model(self, request, obj, form, change):
    NEW_LINE_DELIMITER = "\r\n"

    obj.availability = text_as_json(obj.availability, NEW_LINE_DELIMITER)
    obj.duration = timedelta(hours=obj.duration.seconds)
    obj.itinerary = text_as_json(obj.itinerary, NEW_LINE_DELIMITER)
    obj.description = text_as_json(obj.description, NEW_LINE_DELIMITER)
    obj.included = text_as_json(obj.included, NEW_LINE_DELIMITER)
    obj.requirements = text_as_json(obj.requirements, NEW_LINE_DELIMITER)
    obj.gear = text_as_json(obj.gear, NEW_LINE_DELIMITER)
    obj.additional = text_as_json(obj.additional, NEW_LINE_DELIMITER)
    obj.save()

  def get_form(self, request, obj=None, **kwargs):
    return super(ExperienceAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Category)
