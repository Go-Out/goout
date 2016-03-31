from django.shortcuts import render
from django.core.mail import EmailMessage

def index(request):
  return render(request, "app/index.html", {})

def about(request):
  return render(request, "app/about.html", {})

def team_building(request):
  return render(request, "app/team_building.html", {})

def terms(request):
  return render(request, "app/terms_conditions.html", {})

def consultancy(request):
  message = "<p>" + request.POST.get('name') + "</p>"
  message += "<p>" +  request.POST.get('email') + "</p>"
  message += "<p>" +  request.POST.get('phone') + "</p>"
  message += "<p>" +  request.POST.get('participants', '') + "</p>"
  message += "<p>" +  request.POST.get('date', '') + "</p>"
  message += "<p>" +  request.POST.get('comments', '') + "</p>"

  msg = EmailMessage("Team Building Consultancy", message, "contact@goout.mx", ["contact@goout.mx"])
  msg.content_subtype = "html"
  msg.send()

  return render(request, "app/team_building_confirmation.html", {})
