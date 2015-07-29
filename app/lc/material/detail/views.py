from django.shortcuts import render


def update(request,_id):
  return render(request,get_template("update.html"), {})


def read(request, _id):
  return render(request,get_template("read.html"), {})

def get_template(filename):
  return "material/detail/"+filename