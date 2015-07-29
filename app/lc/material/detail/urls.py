from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^/?$', views.read, name='material.read'),
  url(r'^/update', views.update, name='material.update')
]
