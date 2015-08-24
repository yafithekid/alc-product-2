from django.http import HttpRequest
from django.http.response import HttpResponseNotAllowed, HttpResponseForbidden
from lc.containers import lc_service_container
from lc.course.api.services import CourseService
from user.auth.api.services import AuthService
from user.collections import User
from user.containers import user_service_container


class CourseAuthorization(object):
    WRITE = "write"
    READ = "read"

    def __init__(self, min_level):
        self.min_level = min_level

    def __call__(self, f):
        def do_filter(request: HttpRequest, **kwargs):
            deny = True
            course_service = get_course_service()
            auth_service = get_auth_service()
            user_id = auth_service.get_value("_id", request.session)
            course = course_service.find_by_id(kwargs["_id"])
            # Admin can do anything
            if auth_service.is_authorized_for(request.session, User.ADMIN):
                deny = False
            # Teacher must check if he/she has privileges
            elif auth_service.is_authorized_for(request.session, User.TEACHER):
                if self.min_level == CourseAuthorization.READ:
                    deny = not (course_service.can_read_course(user_id, course))
                else:
                    deny = not (course_service.can_write_course(user_id,course))
            if not deny:
                return f(request, **kwargs)
            else:
                return HttpResponseForbidden()

        return do_filter


def get_auth_service():
    auth_service = user_service_container.load(AuthService.__name__)
    assert isinstance(auth_service, AuthService)
    return auth_service


def get_course_service():
    course_service = lc_service_container.load(CourseService.__name__)
    assert isinstance(course_service, CourseService)
    return course_service
