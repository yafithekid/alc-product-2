from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/info', views.info, name='course.info'),
    url(r'^/update', views.update, name='course.update'),
    url(r'^/join', views.join, name='course.join'),
    url(r'^/?$', views.read, name='course.read')
]
