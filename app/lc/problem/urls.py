from django.conf.urls import url

from . import views

urlpatterns = [
  # ex: /polls/
  url(r'^/read$',views.read,name='read'),
  url(r'^/?$',views.index, name='index')
]