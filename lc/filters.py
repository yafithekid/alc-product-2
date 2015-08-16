from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from user.auth.api.services import AuthService
from user.containers import user_service_container


class Authorized(object):
    def __init__(self, min_role=None):
        self.min_role = min_role

    def __call__(self, f):
        def do_filter(request):
            auth_service = user_service_container.load(AuthService.__name__)
            assert (isinstance(auth_service, AuthService))
            if not auth_service.is_logged_in(request.session):
                return HttpResponseRedirect(reverse('login') + "?next=" + request.path + "")
            else:
                if not (self.min_role is None) and not auth_service.is_authorized_for(request.session, self.min_role):
                    return HttpResponseForbidden()
                else:
                    return f(request)

        return do_filter
