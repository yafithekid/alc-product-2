from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^/?$', views.read, name='tryout.read'),
  url(r'^/info', views.info, name='tryout.info'),
  url(r'^/join', views.join, name='tryout.join')

]