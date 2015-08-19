from django.conf.urls import url, include

from . import views
from .detail import urls as detail_urls
urlpatterns = [
  url(r'^/create$', views.create, name='course.create'),
  url(r'^/(?P<_id>[0-9A-Za-z]+)', include(detail_urls)),
  url(r'^/?$', views.index, name='course.index')
]
