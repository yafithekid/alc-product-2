from django.conf.urls import url,include

from . import views
from lc.problem import urls as problem_urls
from lc.tryout import urls as tryout_urls

urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index, name='index')
    url(r'^problem/$',include(problem_urls)),
    url(r'^tryout/$',include(tryout_urls))
]