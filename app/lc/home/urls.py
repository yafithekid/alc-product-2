from django.conf.urls import url

from . import views

urlpatterns = [
  # ex: /polls/
  url(r'^/register',views.register,name='home.register'),
  url(r'^/login',views.login, name='home.login'),
  url(r'^/confirm-register/(?P<_id>[0-9A-Za-z]+)',views.confirm_register,name='home.confirm_register'),
  url(r'^/?$',views.home,name='home')
]