from django.shortcuts import render


def update(request):
  return render(request, "profile/update.html", {})
