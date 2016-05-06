# -*- coding: UTF-8 -*-

from .. models import Experience, Code
from django.shortcuts import render, redirect
import conekta
from . util import experience_as_json
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.mail import EmailMessage
import os

def payment(request, experience_id):
  date = request.GET.get('date')
  people = request.GET.get('people')
  experience_model = Experience.objects.get(pk=experience_id)

  if date and people and people.isdigit():
    experience = experience_as_json(experience_model)
    return render(request, "app/payment.html", {'experience': experience})
  else:
    return redirect("detail", experience_model.id)

def process_payment(request):
  conekta.api_key = os.environ['CONEKTA_KEY']

  token = request.POST.get("conektaTokenId")
  birth = request.POST.get("birthDate") + "-" + request.POST.get("birthMonth") + "-" + request.POST.get("birthYear")
  name = request.POST.get("name")
  email = request.POST.get("email")
  phone = request.POST.get("phone")
  date = request.POST.get("date")
  people = request.POST.get("people")
  price = request.POST.get("price")
  experience = request.POST.get("experience")
  location = request.POST.get("location")
  code = None

  if not token:
    return redirect("index")

  charge = process_charge(token, name, email, phone, float(price), int(people), experience)

  if charge.status == "paid":
    code = Code.objects.filter(available=True)[:1][0].code
    send_user_email(name, email, experience, location, date, people, price, code)
    send_our_email(name, email, experience, location, date, people, price, phone, birth, code)

  return render(request, "app/payment_confirmation.html", {'charge': charge, 'email': email, 'code': code})

def test_payment(request):
  return render(request, "app/payment_test.html", {})

def process_test(request):
  conekta.api_key = os.environ['CONEKTA_KEY']

  token = request.POST.get("conektaTokenId")
  birth = request.POST.get("birthDate") + "-" + request.POST.get("birthMonth") + "-" + request.POST.get("birthYear")
  name = request.POST.get("name")
  email = request.POST.get("email")
  phone = request.POST.get("phone")
  date = request.POST.get("date")
  people = request.POST.get("people")
  price = request.POST.get("price")
  experience = request.POST.get("experience")
  location = request.POST.get("location")
  code = None

  if not token:
    return redirect("index")

  charge = process_charge(token, name, email, phone, float(price), int(people), experience)

  if charge.status == "paid":
    code = Code.objects.filter(available=True)[:1][0].code

  return render(request, "app/payment_confirmation.html", {'charge': charge, 'email': email, 'code': code})


def process_charge(token, name, email, phone, price, people, experience):
  return conekta.Charge.create({
    "description": experience,
    "amount": price * 100,
    "currency": "MXN",
    "reference_id": email,
    "card": token,
    "details": {
      "name": name,
      "phone": phone,
      "email": email,
      "customer": {},
      "line_items": [{
        "name": experience,
        "description": experience,
        "unit_price": price / people,
        "quantity": 1,
        "sku": "",
        "category": "experience"
        }],
      "billing_address": {
        "street1": "null",
        "street2": "null",
        "street3": "null",
        "city": "null",
        "state": "null",
        "zip": "null",
        "country": "null",
        "tax_id": "null",
        "company_name":"null",
        "phone": "null",
        "email": "null"
        }
      }
    })

def send_user_email(name, email, experience, location, date, people, price, code):
  email_template = open("app/static/app/html/email.html").read().decode("utf-8")
  email_template = email_template.replace("$name", name)
  email_template = email_template.replace("$experience", experience)
  email_template = email_template.replace("$location", location)
  email_template = email_template.replace("$date", date)
  email_template = email_template.replace("$people", people)
  email_template = email_template.replace("$price", "$" + price)
  email_template = email_template.replace("$code", code)

  msg = EmailMessage("Confirmación de ".decode("utf-8") + experience, email_template, "GoOut <contact@goout.mx>", [email])
  msg.content_subtype = "html"
  msg.send()

def send_our_email(name, email, experience, location, date, people, price, phone, birth, code):
  email_template = open("app/static/app/html/email_us.html").read().decode("utf-8")
  email_template = email_template.replace("$name", name)
  email_template = email_template.replace("$experience", experience)
  email_template = email_template.replace("$location", location)
  email_template = email_template.replace("$date", date)
  email_template = email_template.replace("$people", people)
  email_template = email_template.replace("$price", price)
  email_template = email_template.replace("$email", email)
  email_template = email_template.replace("$phone", phone)
  email_template = email_template.replace("$birth", birth)
  email_template = email_template.replace("$code", code)

  msg = EmailMessage("Compra de " + experience, email_template, "GoOut <order@goout.mx>", ["order@goout.mx"])
  msg.content_subtype = "html"
  msg.send()
