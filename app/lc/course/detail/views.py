from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def read(request, _id):
  return render(request, get_template("read.html"), {})


def info(request, _id):
  return render(request, get_template("info.html"), {})


def join(request, _id):
  pass


def get_template(filename):
  return "course/detail/"+filename;
