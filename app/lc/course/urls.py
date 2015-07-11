from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /polls/
  url(r'^/(?P<_id>[0-9A-Za-z]+)',views.read,name='course.read'),
	url(r'^/?$', views.index, name='course.index')
]