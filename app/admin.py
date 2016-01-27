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
      self.initial['description'] = json_as_text(self.instance.description)
      self.initial['duration'] = self.instance.duration.seconds / 3600
      self.initial['requirements'] = json_as_text(self.instance.requirements)
      self.initial['included'] = json_as_text(self.instance.included)
      self.initial['additional'] = json_as_text(self.instance.additional)
      self.initial['benefits'] = json_as_text(self.instance.additional)
      self.initial['gear'] = json_as_text(self.instance.additional)

class ExperienceAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'location')
  form = ExperienceForm

  def save_model(self, request, obj, form, change):
    obj.description = text_as_json(obj.description)
    obj.duration = timedelta(hours=obj.duration.seconds)
    obj.requirements = text_as_json(obj.requirements)
    obj.included = text_as_json(obj.included)
    obj.additional = text_as_json(obj.additional)
    obj.benefits = text_as_json(obj.benefits)
    obj.gear = text_as_json(obj.gear)
    obj.save()

  def get_form(self, request, obj=None, **kwargs):
    print "Hello!" 
    return super(ExperienceAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Category)
