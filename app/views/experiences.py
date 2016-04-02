from django.shortcuts import render
from django.http import JsonResponse
from .. models import Experience, Category
from datetime import date
from . util import experience_as_json

def experiences_json(request):
  category = request.GET.get('category').replace("_", " ");

  experience_models = Experience.objects.filter(active=True, categories__name=category)
  experiences = map(experience_as_json, experience_models)

  return JsonResponse(experiences, safe=False)

def detail(request, experience_id):
  experience_model = Experience.objects.get(pk=experience_id)

  experience = experience_as_json(experience_model)

  context = {'experience': experience}
  return render(request, "app/detail.html", context)

def experience_availability(request, experience_id):
  day = getDateDay(request.GET.get('date'))

  experience_model = Experience.objects.get(pk=experience_id)
  experience = experience_as_json(experience_model)

  context = {'available': isExperienceAvailable(experience, day)}
  return JsonResponse(context)


def isExperienceAvailable(experience, day):
  return day in experience["availability"] or not experience["availability"]

def getDateDay(date_str):
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  dates = date_str.split("-")
  d = date(int(dates[0]), int(dates[1]), int(dates[2]))
  return days[d.weekday()]