from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^/?$', views.read, name='problem.read'),
  url(r'^/discuss', views.discuss, name='problem.discuss')
]
