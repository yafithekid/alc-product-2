from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^/contact', views.contact, name='contact'),
    url(r'^/about', views.about, name='about'),
    url(r'^/register', views.register, name='register'),
    url(r'^/login', views.login, name='login'),
    url(r'^/logout', views.logout, name='logout'),
    url(r'^/confirm-register/(?P<_id>[0-9A-Za-z]+)', views.confirm_register, name='confirm_register'),
    url(r'^/?$', views.home, name='home')
]
