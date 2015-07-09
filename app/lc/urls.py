from django.conf.urls import url,include

from app.lc.problem import urls as problem_urls
from app.lc.home import urls as home_urls

urlpatterns = [
  # ex: /polls/
  #url(r'^$', views.index, name='index')
  url(r'^/problem',include(problem_urls)),
  url(r'^',include(home_urls))
]