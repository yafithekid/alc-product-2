from django.shortcuts import render


# Create your views here.
def index(request):
  return render(request, get_template("index.html"), {})


def create(request):
  return render(request, get_template("create.html"), {})


def get_template(filename):
  return "tryout/" + filename
