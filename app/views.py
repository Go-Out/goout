from django.shortcuts import render
from django.http import JsonResponse
from .models import Experience, Category
from django.core import serializers
import json
import conekta

# Create your views here.
def index(request):
  experiences = Experience.objects.all()
  context = {'experiences': experiences}
  return render(request, "app/index.html", context)

def experiences_json(request):
  date = request.GET.get('date')
  experiences = map(experience_as_json, Experience.objects.all())
  return JsonResponse(experiences, safe=False)

def detail(request, experience_id):
  experience_model = Experience.objects.get(pk=experience_id)

  context = {'experience': experience_as_json(experience_model)}
  return render(request, "app/detail.html", context)

def json_detail(request, experience_id):
  experience_model = Experience.objects.get(pk=experience_id)

  return JsonResponse(experience_as_json(experience_model))

def payment(request, experience_id):
  return render(request, "app/payment.html", {'experience_id': experience_id})

def process_payment(request, experience_id):
  conekta.api_key = "key_fhT3iSqcYrPfsqpuggUZRQ"
  charge = conekta.Charge.create({
    "description":"Stogies",
    "amount": 20000,
    "currency":"MXN",
    "reference_id":"9839-wolf_pack",
    "card": "tok_test_visa_4242",
    "details": {
      "name": "Arnulfo Quimare",
      "phone": "403-342-0642",
      "email": "logan@x-men.org",
      "customer": {
        "logged_in": "true",
        "successful_purchases": 14,
        "created_at": 1379784950,
        "updated_at": 1379784950,
        "offline_payments": 4,
        "score": 9
      },
      "line_items": [{
        "name": "Box of Cohiba S1s",
        "description": "Imported From Mex.",
        "unit_price": 20000,
        "quantity": 1,
        "sku": "cohb_s1",
        "category": "food"
      }],
      "billing_address": {
        "street1":"77 Mystery Lane",
        "street2": "Suite 124",
        "street3": "null",
        "city": "Darlington",
        "state":"NJ",
        "zip": "10192",
        "country": "Mexico",
        "tax_id": "xmn671212drx",
        "company_name":"X-Men Inc.",
        "phone": "77-777-7777",
        "email": "purshasing@x-men.org"
      }
    }
  })
  return render(request, "app/payment_result.html", {'charge': charge})

def experience_as_json(experience_model):
  experience = serializers.serialize("python", [experience_model,])[0]["fields"]

  experience["id"] = experience_model.id
  experience["description"] = json.loads(experience_model.description)
  experience["availability"] = json.loads(experience_model.availability)
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
