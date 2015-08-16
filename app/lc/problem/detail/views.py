from django.http import HttpResponseNotFound
from django.shortcuts import render
from lc.containers import lc_service_container
from lc.problem.api.services import ProblemService
from user.api.services import UserService
from user.containers import user_service_container


def read(request, _id):
    problem_service = lc_service_container.load(ProblemService.__name__)
    user_service = user_service_container.load(UserService.__name__)
    assert (isinstance(problem_service, ProblemService))
    assert (isinstance(user_service,UserService))
    problem = problem_service.find_by_id(_id)
    if problem is None:
        return HttpResponseNotFound()
    else:
        user = user_service.find_by_id(problem.creator_id)
        return render(request, get_template("read.html"), {"problem": problem,"user" : user})


def discuss(request, _id):
    return render(request, get_template("discuss.html"), {})


def get_template(filename):
    return "problem/detail/" + filename
