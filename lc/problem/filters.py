from django.http import HttpRequest, HttpResponseNotFound
from lc.containers import lc_service_container
from lc.problem.api.services import ProblemService
from user.auth.api.services import AuthService
from user.containers import user_service_container


class AuthorizedForProblemView(object):
    def __call__(self, f):
        def do_filter(request: HttpRequest, **kwargs):
            problem_service = get_problem_service()
            problem = problem_service.find_by_id(kwargs["_id"])
            # TODO impl
            return f(request, **kwargs)

        return do_filter


def get_problem_service():
    problem_service = lc_service_container.load(ProblemService.__name__)
    assert isinstance(problem_service, ProblemService)
    return problem_service


def get_auth_service():
    auth_service = user_service_container.load(AuthService.__name__)
    assert isinstance(auth_service, AuthService)
    return auth_service
