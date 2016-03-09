from django.shortcuts import render
from django.http import JsonResponse
from .models import Experience, Category
from django.core import serializers
import json
from datetime import date

# Create your views here.
def index(request):
  return render(request, "app/index.html", {})

def experiences_json(request):
  day = getDateDay(request.GET.get('date'))

  experience_models = Experience.objects.all()
  experiences = map(experience_as_json, experience_models)

  experiences = filter(lambda experience: isExperienceAvailable(experience, day), experiences)

  return JsonResponse(experiences, safe=False)

def detail(request, experience_id):
  experience_model = Experience.objects.get(pk=experience_id)

  context = {'experience': experience_as_json(experience_model)}
  return render(request, "app/detail.html", context)

def experience_availability(request, experience_id):
  day = getDateDay(request.GET.get('date'))

  experience_model = Experience.objects.get(pk=experience_id)
  experience = experience_as_json(experience_model)

  context = {'available': isExperienceAvailable(experience, day)}
  return JsonResponse(context)

def about(request):
  return render(request, "app/about.html", {})

def team_building(request):
  return render(request, "app/team_building.html", {})


def experience_as_json(experience_model):
  experience = serializers.serialize("python", [experience_model,])[0]["fields"]

  experience["id"] = experience_model.id
  experience["price"] = float(experience_model.price)
  experience["availability"] = json.loads(experience_model.availability)
  experience["duration"] = experience_model.duration.seconds / 3600
  experience["description"] = json.loads(experience_model.description)
  experience["itinerary"] = json.loads(experience_model.itinerary)
  experience["included"] = json.loads(experience_model.included)
  experience["requirements"] = json.loads(experience_model.requirements)
  experience["gear"] = json.loads(experience_model.gear)
  experience["additional"] = json.loads(experience_model.additional) 
  experience["images"] = experience_model.images
  categories = []
  category_pks = experience["categories"]
  for category_pk in category_pks:
    category = Category.objects.get(pk=category_pk).name
    categories.append(category)
  experience["categories"] = categories

  return experience

def isExperienceAvailable(experience, day):
  return day in experience["availability"] or not experience["availability"]

def getDateDay(date_str):
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  dates = date_str.split("-")
  d = date(int(dates[0]), int(dates[1]), int(dates[2]))
  return days[d.weekday()]
