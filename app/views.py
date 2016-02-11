from django.shortcuts import render
from django.http import JsonResponse
from .models import Experience, Category
from django.core import serializers
import json

# Create your views here.
def index(request):
  experiences = Experience.objects.all()
  context = {'experiences': experiences}
  return render(request, "app/experiences.html", context)

def detail(request, experience_id):
  experience_model = Experience.objects.get(pk=experience_id)

  context = {'experience': experience_as_json(experience_model)}
  return render(request, "app/detail.html", context)

def json_detail(request, experience_id):
  experience_model = Experience.objects.get(pk=experience_id)

  return JsonResponse(experience_as_json(experience_model))


def experience_as_json(experience_model):
  experience = serializers.serialize("python", [experience_model,])[0]["fields"]

  experience["description"] = json.loads(experience_model.description)
  experience["price"] = float(experience_model.price)
  experience["duration"] = experience_model.duration.seconds / 3600
  experience["requirements"] = json.loads(experience_model.requirements)
  experience["included"] = json.loads(experience_model.included)
  experience["additional"] = json.loads(experience_model.additional) 
  experience["benefits"] = json.loads(experience_model.benefits)
  experience["gear"] = json.loads(experience_model.gear)

  categories = []
  category_pks = experience["categories"]
  for category_pk in category_pks:
    category = Category.objects.get(pk=category_pk).name
    categories.append(category)
  experience["categories"] = categories

  return experience
