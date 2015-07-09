from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from . import forms
from user.services import UserService
# Create your views here.
def register(request):
  if request.method == 'POST':
    form = forms.RegisterForm(request.POST)
    if (form.is_valid()):
      print(form.cleaned_data['email'])
      user = UserService.register(form.cleaned_data['email'],form.cleaned_data['name'],form.cleaned_data['password'])
      return HttpResponseRedirect(reverse('confirm_register',args=[str(user.id)]))
    else:
      return render(request,'home/register.html',{'form':form})
  else:
    form = forms.RegisterForm()
    return render(request,'home/register.html',{'form':form})

def confirm_register(request,_id):
  user = UserService.findById(_id)
  return render(request,'home/confirm_register.html',{'user':user})

def login(request):
  return HttpResponse("login")