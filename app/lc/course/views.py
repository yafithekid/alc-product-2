from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
from app.lc.course.forms import CourseForm
from lc.collections import Course
from lc.containers import lc_service_container
from lc.course.api.services import CourseService
from lc.filters import Authorized
from user.auth.api.services import AuthService
from user.collections import User
from user.containers import user_service_container


def index(request):
    course_service = get_course_service()
    res = course_service.paginate({}, [], 1, request)
    return render(request, "course/index.html", {"res": res})


@Authorized(min_role=User.TEACHER)
def create(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = Course.from_form(form)
            auth_service = get_auth_service()
            user_id = auth_service.get_value("_id", request.session)
            course.creator_id = user_id
            course_service = get_course_service()
            course_id = course_service.add_course(course)
            if not (course_id is None):
                return HttpResponseRedirect(reverse("course.info", args=[course_id]))

    return render(request, "course/create.html",
                  {"form": form, "public_course": Course.PUBLIC, "private_course": Course.PRIVATE})


def get_auth_service():
    auth_service = user_service_container.load(AuthService.__name__)
    assert isinstance(auth_service, AuthService)
    return auth_service


def get_course_service():
    course_service = lc_service_container.load(CourseService.__name__)
    assert isinstance(course_service, CourseService)
    return course_service
