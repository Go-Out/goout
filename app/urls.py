from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^experiences/json$', views.experiences_json, name='experiences_json'),
  url(r'^experiences/(?P<experience_id>[0-9]+)$', views.detail, name='detail'),
  url(r'^experiences/(?P<experience_id>[0-9]+)/payment$', views.payment, name='payment'),
  url(r'^process_payment/(?P<experience_id>[0-9]+)$', views.process_payment, name='process_payment'),
  url(r'^experiences/(?P<experience_id>[0-9]+)/availability$', views.experience_availability, name='experience_availability'),
  url(r'^about$', views.about, name='about'),
  url(r'^team-building$', views.team_building, name='team_building'),
  url(r'^consultancy$', views.consultancy, name='consultancy'),
  url(r'^terms$', views.terms, name='terms'),
]
