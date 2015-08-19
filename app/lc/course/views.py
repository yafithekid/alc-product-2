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
    return render(request, "course/index.html", {})


def read(request, _id):
    return render(request, "course/read.html", {})


@Authorized(min_role=User.TEACHER)
def create(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = Course.from_form(form)
            auth_service = user_service_container.load(AuthService.__name__)
            assert isinstance(auth_service, AuthService)
            user_id = auth_service.get_value("_id", request.session)
            course.creator_id = user_id
            course_service = lc_service_container.load(CourseService.__name__)
            assert isinstance(course_service, CourseService)
            course_id = course_service.add_course(course)
            if not (course_id is None):
                return HttpResponseRedirect(reverse("course.info", args=[course_id]))

    return render(request, "course/create.html",
                  {"form": form, "public_course": Course.PUBLIC, "private_course": Course.PRIVATE})


def join(request):
    pass
