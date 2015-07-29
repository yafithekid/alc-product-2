from django.shortcuts import render


def read(request, _id):
  return render(request, get_template("read.html"), {})


def discuss(request, _id):
  return render(request, get_template("discuss.html"), {})


def get_template(filename):
  return "problem/detail/" + filename
