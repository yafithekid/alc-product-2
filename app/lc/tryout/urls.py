from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /polls/
  url(r'^/(?P<_id>[0-9A-Za-z]+)/info',views.info,name='tryout.info'),
  url(r'^/(?P<_id>[0-9A-Za-z]+)',views.read,name='tryout.read'),
	url(r'^/?$', views.index, name='tryout.index')
]