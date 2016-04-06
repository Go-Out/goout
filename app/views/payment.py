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

  if charge.status == 'paid':
    send_email()

  return render(request, "app/payment_confirmation.html", {'charge': charge, 'email': request.POST.get('email')})


def send_email():
  email_template = open("app/static/app/html/email.html").read()

  msg = EmailMessage("Test", email_template, "contact@goout.mx", ["lsgaleana@gmail.com"])
  msg.content_subtype = "html"
  msg.send()
