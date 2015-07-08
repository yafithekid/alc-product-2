from django.shortcuts import render
from lc.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
  user = User(email="test@gmail.com",name="test",password="test")
  user.save()
  problem = Problem(slug="mboh" + str(user.id),title="test",description="woi",author=user.id)
  problem.save()
  return HttpResponse("Hello world, your new id is =" + str(user.id))