from django.shortcuts import render
from django.http import JsonResponse
from .models import Experience, Category, Demographic
from django.core import serializers
import json

# Create your views here.
def index(request):
  return HttpResponse('Welcome to goout!')

def experiences(request):
  experiences = Experience.objects.all()
  context = {'experiences': experiences}
  return render(request, "app/experiences.html", context)

def detail(request, experience_id):
  experience_model = Experience.objects.get(pk=experience_id)
  duration = experience_model.duration.seconds / 3600
  requirements = json.loads(experience_model.requirements)
  included = json.loads(experience_model.included)
  additional = json.loads(experience_model.additional)

  experience = serializers.serialize("python", [experience_model,])[0]["fields"]

  experience["duration"] = duration
  experience["requirements"] = requirements
  experience["included"] = included
  experience["additional"] = additional 

  categories = []
  category_pks = experience["categories"]
  for category_pk in category_pks:
    category = Category.objects.get(pk=category_pk).name
    categories.append(category)
  experience["categories"] = categories

  demographics = []
  demographic_pks = experience["demographics"]
  for demographic_pk in demographic_pks:
    demographic = Demographic.objects.get(pk=demographic_pk).name
    demographics.append(demographic)
  experience["demographics"] = demographics 

  return JsonResponse(experience)
