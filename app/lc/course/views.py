from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	return render(request,"course/index.html",{})

def read(request,_id):
  return render(request,"course/read.html",{})