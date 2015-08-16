from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from . import forms
from lc.containers import lc_service_container
from lc.filters import Authorized
from lc.problem.api.services import ProblemService
from user.api.services import UserService
from user.auth.api.services import AuthService
from user.collections import User
from user.containers import user_service_container


def register(request):
    register_success = False
    user = None
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user_service = user_service_container.load(UserService.__name__)
            assert (isinstance(user_service, UserService))
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                form.add_error("confirm_password", "Password doesn't match")
            elif user_service.find_by_email(email=form.cleaned_data['email']) is None:
                _id = user_service.add_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'],
                                            name=form.cleaned_data['name'])
                return HttpResponseRedirect(reverse('confirm_register', args=[_id]))
            else:
                form.add_error(None, "Email already exist")
    else:
        form = forms.RegisterForm()
    return render(request, 'home/register.html', {'form': form})


def confirm_register(request, _id):
    user_service = user_service_container.load(UserService.__name__)
    assert (isinstance(user_service, UserService))
    user = user_service.find_by_id(_id=_id)
    if user is None:
        return HttpResponseNotFound("User doesn't exist")
    else:
        return render(request, 'home/confirm_register.html', {'user': user})


def login(request):
    login_success = False
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            auth_service = user_service_container.load(AuthService.__name__)
            assert (isinstance(auth_service, AuthService))
            user = auth_service.attempt(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is None:
                form.add_error(None, "Invalid email/password")
            else:
                auth_service.login(user, request.session)
                next_url = request.GET.get('next', reverse('home'))
                return HttpResponseRedirect(next_url)

    else:
        form = forms.LoginForm()
    if not login_success:
        return render(request, 'home/login.html', {'form': form})
    else:
        return HttpResponse("login_success")


@Authorized()
def logout(request):
    auth_service = user_service_container.load(AuthService.__name__)
    assert (isinstance(auth_service, AuthService))
    auth_service.logout(request.session)
    return HttpResponseRedirect(reverse("home"))


def home(request):
    problem_service = lc_service_container.load(ProblemService.__name__)
    assert isinstance(problem_service, ProblemService)
    problem_service.find_by_id("hello_world")
    return render(request, 'home/home.html', {})


@Authorized()
def about(request):
    return render(request, "home/about.html", {})


@Authorized(min_role=User.TEACHER)
def contact(request):
    return render(request, "home/contact.html", {})
