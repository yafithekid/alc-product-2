from django.http import HttpResponseNotFound
from django.shortcuts import render
from lc.collections import Course
from lc.containers import lc_service_container
from lc.course.api.services import CourseService
from lc.course.filters import CourseAuthorization
from lc.filters import Authorized
from user.auth.api.services import AuthService
from user.collections import User
from user.containers import user_service_container


def read(request, _id):
    course_service = get_course_service()
    course = course_service.find_by_id(_id)
    if course is None:
        return HttpResponseNotFound()
    else:
        return render(request, get_template("read.html"), {"course": course})


@Authorized()
def info(request, _id):
    course_service = get_course_service()
    course = course_service.find_by_id(_id)
    if course is None:
        return HttpResponseNotFound()
    else:
        return render(request, "course/detail/info.html", {"course": course})


@Authorized(min_role=User.TEACHER)
@CourseAuthorization(min_level=CourseAuthorization.WRITE)
def update(request, _id):
    course_service = get_course_service()
    course = course_service.find_by_id(_id)
    if course is None:
        return HttpResponseNotFound()
    form = Course.to_form(course)
    return render(request, "course/detail/update.html",
                  {"form": form, "id": _id, "public_course": Course.PUBLIC, "private_course": Course.PRIVATE})


def join(request, _id):
    pass


def get_template(filename):
    return "course/detail/" + filename


def get_course_service():
    course_service = lc_service_container.load(CourseService.__name__)
    assert isinstance(course_service, CourseService)
    return course_service


def get_auth_service():
    auth_service = user_service_container.load(AuthService.__name__)
    assert isinstance(auth_service, AuthService)
    return auth_service
