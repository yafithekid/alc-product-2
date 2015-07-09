from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	template = loader.get_template("problem/index.html")
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def read(request):
	template = loader.get_template("problem/read.html")
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))	