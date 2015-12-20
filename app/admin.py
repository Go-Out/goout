from django.contrib import admin
from .models import Experience, Category, Demographic
from datetime import timedelta
from django import forms

# Register your models here.

class ExperienceForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(ExperienceForm, self).__init__(*args, **kwargs)
    if self.instance.duration is not None:
      self.initial['duration'] = self.instance.duration.seconds / 3600
      self.initial['requirements'] = json_as_text(self.instance.requirements)
      self.initial['included'] = json_as_text(self.instance.included)
      self.initial['additional'] = json_as_text(self.instance.additional)

class ExperienceAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'location')
  form = ExperienceForm

  def save_model(self, request, obj, form, change):
    obj.duration = timedelta(hours=obj.duration.seconds)
    obj.requirements = text_as_json(obj.requirements)
    obj.included = text_as_json(obj.included)
    obj.additional = text_as_json(obj.additional)
    obj.save()

  def get_form(self, request, obj=None, **kwargs):
    print "Hello!" 
    return super(ExperienceAdmin, self).get_form(request, obj, **kwargs)

def text_as_json(text):
  elements = text.splitlines()
  json = "[\"" + elements[0] + "\""
  for i in range(1, len(elements)):
    json += ",\"" + elements[i] + "\""
  json += "]"
  return json

def json_as_text(json):
  return json[2:len(json) - 2].replace("\",\"", "\n")

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Category)
admin.site.register(Demographic)
