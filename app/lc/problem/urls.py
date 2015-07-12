from django.conf.urls import url

from . import views

urlpatterns = [
  # ex: /polls/
  url(r'^/create',views.create,name='problem.create'),
  url(r'^/(?P<_id>[0-9A-Za-z]+)$',views.read,name='problem.read'),
  url(r'^/?$',views.index, name='problem.index')
]