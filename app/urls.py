from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^experiences/$', views.experiences, name='experiences'),
  url(r'^experiences/(?P<experience_id>[0-9]+)/$', views.detail, name='detail'),
]
