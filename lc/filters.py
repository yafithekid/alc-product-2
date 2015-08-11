from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from user.auth.api.services import AuthService
from user.containers import user_service_container


def authenticated(func):
    def do_filter(request):

        auth_service = user_service_container.load(AuthService.__name__)
        assert (isinstance(auth_service, AuthService))
        if auth_service.is_logged_in(request.session):
            return func(request)
        else:
            return HttpResponseRedirect(reverse('login')+"?next="+request.path+"")

    return do_filter

