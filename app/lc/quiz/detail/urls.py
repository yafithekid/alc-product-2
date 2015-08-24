from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^/?$', views.read, name='quiz.read'),
  url(r'^/info', views.info, name='quiz.info'),
  url(r'^/join', views.join, name='quiz.join')

]