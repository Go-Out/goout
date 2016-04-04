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
  experience["images"] = json.dumps(sorted(os.listdir(experience_model.images_path)))
  experience["images_path"] = experience_model.images_path[4:]
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
