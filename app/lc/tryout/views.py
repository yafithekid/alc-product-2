from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	return render(request,"tryout/index.html",{})

def read(request,_id):
  return render(request,"tryout/read.html",{})

def info(request,_id):
  return render(request,"tryout/info.html",{})