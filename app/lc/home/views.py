from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from user.services import UserService
from commons.commands import CommandBus
from user.auth.commands import RegisterUser, LoginUser


def register(request):
  register_success = False

  if request.method == 'POST':
    form = forms.RegisterForm(request.POST)
    if (form.is_valid()):
      bus = CommandBus()
      regUser = RegisterUser(email=form.cleaned_data['email'], password=form.cleaned_data['password'],
                             name=form.cleaned_data['name'])
      bus.execute(regUser)
      user = UserService.findByEmail(form.cleaned_data['email'])
      register_success = True
  else:
    form = forms.RegisterForm()

  if (register_success):
    return HttpResponseRedirect(reverse('home.confirm_register', args=[str(user.id)]))
  else:
    return render(request, 'home/register.html', {'form': form})


def confirm_register(request, _id):
  user = UserService.findById(_id)
  return render(request, 'home/confirm_register.html', {'user': user})


def login(request):
  login_success = False
  if (request.method == 'POST'):
    form = forms.LoginForm(request.POST)
    if (form.is_valid()):
      bus = CommandBus()
      bus.execute(LoginUser(email=form.cleaned_data['email'], request=request))
      login_success = True
  else:
    form = forms.LoginForm()
  if (not login_success):
    return render(request, 'home/login.html', {'form': form})
  else:
    return HttpResponse("login_success")


def home(request):
  return render(request, 'home/home.html', {})

def about(request):
  return render(request, "home/about.html", {})
def contact(request):
  return render(request, "home/contact.html",{})
