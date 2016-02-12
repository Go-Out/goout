from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^experiences/(?P<experience_id>[0-9]+)$', views.detail, name='detail'),
  url(r'^experiences/(?P<experience_id>[0-9]+)/json$', views.json_detail, name='json_detail'),
  url(r'^experiences/(?P<experience_id>[0-9]+)/payment$', views.payment, name='payment'),
]
