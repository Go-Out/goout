from django.core import serializers
import json
import os
from .. models import  Experience, Category

def experience_as_json(experience_model):
  experience = serializers.serialize("python", [experience_model,])[0]["fields"]

  experience["id"] = experience_model.id
  experience["price"] = float(experience_model.price)
  experience["availability"] = json.loads(experience_model.availability)
  experience["duration"] = experience_model.duration.seconds / 3600 if experience_model.duration.seconds else experience_model.duration.days * 24
  experience["description"] = json.loads(experience_model.description)
  experience["itinerary"] = json.loads(experience_model.itinerary)
  experience["included"] = json.loads(experience_model.included)
  experience["requirements"] = json.loads(experience_model.requirements)
  experience["gear"] = json.loads(experience_model.gear)
  experience["additional"] = json.loads(experience_model.additional) 
  experience["images"] = json.dumps(sorted(os.listdir(experience_model.images_path)))
  experience["images_path"] = experience_model.images_path[4:]

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
