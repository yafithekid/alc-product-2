from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	return render(request,"material/index.html",{})

def read(request,_id):
  return render(request,"material/read.html",{})