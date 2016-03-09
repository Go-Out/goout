from django.shortcuts import render
import conekta

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
