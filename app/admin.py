from django.contrib import admin
from .models import Experience, Category, Code
from datetime import timedelta
from django import forms
from .utils import text_as_json, json_as_text
import xmltodict
import urllib2

# Helper method to get an xml list of objects in the s3 repository
def get_image_folders():
  path = "https://s3-us-west-2.amazonaws.com/go-out"

  # Parses every xml tag to obtain the name of the folder
  folders = []
  for content in xmltodict.parse(urllib2.urlopen(path).read())["ListBucketResult"]["Contents"]:
    folder = content["Key"].split("/")[0]
    if (folder, folder) not in folders:
      folders.append((folder, folder))

  return folders

class ExperienceForm(forms.ModelForm):

  # Transforms the model back to display correctly in the admin page
  def __init__(self, *args, **kwargs):
    super(ExperienceForm, self).__init__(*args, **kwargs)
    if self.instance.duration is not None:
      self.initial['availability'] = json_as_text(self.instance.availability)
      self.initial['duration'] = self.instance.duration.seconds / 3600 if self.instance.duration.seconds else self.instance.duration.days * 24
      self.initial['description'] = json_as_text(self.instance.description)
      self.initial['itinerary'] = json_as_text(self.instance.itinerary)
      self.initial['included'] = json_as_text(self.instance.included)
      self.initial['requirements'] = json_as_text(self.instance.requirements)
      self.initial['gear'] = json_as_text(self.instance.gear)
      self.initial['additional'] = json_as_text(self.instance.additional)
    
    self.fields['images_path'] = forms.ChoiceField(choices=get_image_folders())

class ExperienceAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'location', 'active')
  form = ExperienceForm

  # Transforms the model before saving, to create jsons and the right duration
  def save_model(self, request, obj, form, change):
    NEW_LINE_DELIMITER = "\r\n"

    obj.availability = text_as_json(obj.availability, NEW_LINE_DELIMITER)
    obj.duration = timedelta(hours=obj.duration.seconds)  # Makes sure that the time is saved in hours
    obj.itinerary = text_as_json(obj.itinerary, NEW_LINE_DELIMITER)
    obj.description = text_as_json(obj.description, NEW_LINE_DELIMITER)
    obj.included = text_as_json(obj.included, NEW_LINE_DELIMITER)
    obj.requirements = text_as_json(obj.requirements, NEW_LINE_DELIMITER)
    obj.gear = text_as_json(obj.gear, NEW_LINE_DELIMITER)
    obj.additional = text_as_json(obj.additional, NEW_LINE_DELIMITER)
    obj.save()

  def get_form(self, request, obj=None, **kwargs):
    return super(ExperienceAdmin, self).get_form(request, obj, **kwargs)


class CodeAdmin(admin.ModelAdmin):
  list_display = ('code', 'available')
  ordering = ('available',)


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Category)
admin.site.register(Code, CodeAdmin)
