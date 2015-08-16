from django.shortcuts import render
from lc.containers import lc_service_container
from lc.problem.api.services import ProblemService


def read(request, _id):
    problem_service = lc_service_container.load(ProblemService.__name__)
    assert (isinstance(problem_service, ProblemService))
    problem = problem_service.find_by_id(_id)
    return render(request, get_template("read.html"), {"problem": problem})


def discuss(request, _id):
    return render(request, get_template("discuss.html"), {})


def get_template(filename):
    return "problem/detail/" + filename
