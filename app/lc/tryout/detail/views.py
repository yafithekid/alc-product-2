from django.shortcuts import render


def read(request, _id):
  print("read")
  return render(request, get_template("read.html"), {})


def info(request, _id):
  print("info")
  return render(request, get_template("info.html"), {})


def join(request, _id):
  return render(request, get_template("join.html"), {})


def get_template(filename):
  return "tryout/detail/" + filename
