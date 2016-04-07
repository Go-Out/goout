from .. models import Experience
from django.shortcuts import render, redirect
import conekta
from . util import experience_as_json
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.mail import EmailMessage

def payment(request, experience_id):
  date = request.GET.get('date')
  people = request.GET.get('people')
  experience_model = Experience.objects.get(pk=experience_id)

  if date and people and people.isdigit():
    experience = experience_as_json(experience_model)
    return render(request, "app/payment.html", {'experience': experience})
  else:
    return redirect("detail", experience_model.id)

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

  birth = request.POST.get("birthDate") + "-" + request.POST.get("birthMonth") + "-" + request.POST.get("birthYear")
  name = request.POST.get("name")
  email = request.POST.get("email")
  phone = request.POST.get("phone")
  date = request.POST.get("date")
  people = request.POST.get("people")
  price = request.POST.get("price")
  experience = request.POST.get("experience")
  location = request.POST.get("location")

  if charge.status == "paid":
    send_user_email(name, email, experience, location, date, people, price)

  return render(request, "app/payment_confirmation.html", {'charge': charge, 'email': email})


def send_user_email(name, email, experience, location, date, people, price):
  email_template = open("app/static/app/html/email.html").read().decode("utf-8")
  email_template = email_template.replace("$name", name)
  email_template = email_template.replace("$experience", experience)
  email_template = email_template.replace("$location", location)
  email_template = email_template.replace("$date", date)
  email_template = email_template.replace("$people", people)
  email_template = email_template.replace("$price", price)

  msg = EmailMessage(experience + " confirmation", email_template, "contact@goout.mx", [email])
  msg.content_subtype = "html"
  msg.send()
