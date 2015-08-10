from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from lc.containers import lc_service_container
from lc.problem.api.services import ProblemService
from user.api.daos import UserDao
from user.api.services import UserService
from user.collections import User
from user.containers import user_service_container, user_dao_container


def register(request):
    register_success = False
    user = None
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user_service = user_service_container.load(UserService.__name__)
            assert (isinstance(user_service,UserService))
            user = user_service.add_user(email=form.cleaned_data['email'],password=form.cleaned_data['password'],name=form.cleaned_data['name'])
            register_success = True
    else:
        form = forms.RegisterForm()

    if (register_success):
        return HttpResponseRedirect(reverse('home.confirm_register', args=[str(user._id)]))
    else:
        return render(request, 'home/register.html', {'form': form})


def confirm_register(request, _id):
    # user_service = user_service_container.load(UserService.__name__)
    # assert (isinstance(user_service,UserService))
    # user = UserService.findById(_id)

    return render(request, 'home/confirm_register.html', {'user': user})


def login(request):
    login_success = False


    if (request.method == 'POST'):
        form = forms.LoginForm(request.POST)
        if (form.is_valid()):
            user_service = user_service_container.load(UserService.__name__)
            assert(isinstance(user_service,UserService))
            user = authenticate(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            if user is None:
                raise Exception("Invalid username/password")
            else:
                return HttpResponse("login_success")
            login_success = True
    else:
        form = forms.LoginForm()
    if (not login_success):
        return render(request, 'home/login.html', {'form': form})
    else:
        return HttpResponse("login_success")


def home(request):
    problem_service = lc_service_container.load(ProblemService.__name__)
    assert isinstance(problem_service, ProblemService)
    problem_service.findById("hello_world")
    return render(request, 'home/home.html', {})


def about(request):
    return render(request, "home/about.html", {})


def contact(request):
    return render(request, "home/contact.html", {})
