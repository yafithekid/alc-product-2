from django.conf.urls import url,include

from app.lc.problem import urls as problem_urls
from app.lc.home import urls as home_urls
from app.lc.tryout import urls as tryout_urls
from app.lc.course import urls as course_urls
from app.lc.material import urls as material_urls

urlpatterns = [
  # ex: /polls/
  #url(r'^$', views.index, name='index')
  url(r'^/problem',include(problem_urls)),
  url(r'^/tryout',include(tryout_urls)),
  url(r'^/course',include(course_urls)),
  url(r'^/material',include(material_urls)),
  url(r'^',include(home_urls))
]