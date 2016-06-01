from django.core import serializers
import json
import os
from .. models import  Experience, Category
import xmltodict
import urllib2

# Transforms an experience model into a json
def experience_as_json(experience_model):
  experience = serializers.serialize("python", [experience_model,])[0]["fields"]

  experience["id"] = experience_model.id
  experience["price"] = float(experience_model.price)
  experience["availability"] = json.loads(experience_model.availability)
  # For some reason, the time is sometimes stored in 'seconds' and sometimes in 'fields'. The right value is taken here
  experience["duration"] = experience_model.duration.seconds / 3600 if experience_model.duration.seconds else experience_model.duration.days * 24
  experience["description"] = json.loads(experience_model.description)
  experience["itinerary"] = json.loads(experience_model.itinerary)
  experience["included"] = json.loads(experience_model.included)
  experience["requirements"] = json.loads(experience_model.requirements)
  experience["gear"] = json.loads(experience_model.gear)
  experience["additional"] = json.loads(experience_model.additional) 

  categories = []
  category_pks = experience["categories"]
  for category_pk in category_pks:
    category = Category.objects.get(pk=category_pk).name
    categories.append(category)
  experience["categories"] = categories

  experience_prices = []
  experience_pks = experience["experiences"]
  for experience_pk in experience_pks:
    experience_price = str(Experience.objects.get(pk=experience_pk).price)
    experience_prices.append(experience_price)
  experience["experience_prices"] = json.dumps(experience_prices)

  return experience

# Returns all the images for a given experience images folder
def get_experience_images(folder):
  path = "https://s3-us-west-2.amazonaws.com/go-out"
  xml = urllib2.urlopen(path).read()

  images = []
  for content in xmltodict.parse(xml)["ListBucketResult"]["Contents"]:
    if folder in content["Key"] and int(content["Size"]) > 0:
      images.append(content["Key"].replace(" ", "+"))

  return images

# Returns the first experience for the given images folders
def get_experiences_images(folders):
  path = "https://s3-us-west-2.amazonaws.com/go-out"
  xml = urllib2.urlopen(path).read()

  images = []
  for folder in folders:
    for content in xmltodict.parse(xml)["ListBucketResult"]["Contents"]:
      if folder in content["Key"] and int(content["Size"]) > 0:
        images.append(content["Key"].replace(" ", "+"))
        break

  return images
