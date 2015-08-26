from django.http import HttpRequest, HttpResponseForbidden
from lc.containers import lc_service_container
from lc.material.api.services import MaterialService
from user.auth.api.services import AuthService
from user.collections import User
from user.containers import user_service_container


class MaterialAuthorization(object):
    WRITE = "write"
    READ = "read"

    def __init__(self, min_level):
        self.min_level = min_level

    def __call__(self, f):
        def do_filter(request: HttpRequest, **kwargs):
            deny = True
            material_service = get_material_service()
            auth_service = get_auth_service()
            user_id = auth_service.get_value("_id", request.session)
            material = material_service.find_by_id(kwargs["_id"])
            # Admin can do anything
            if auth_service.is_authorized_for(request.session, User.ADMIN):
                deny = False
            # Teacher must check if he/she has privileges
            elif auth_service.is_authorized_for(request.session, User.TEACHER):
                if self.min_level == self.READ:
                    deny = not (material_service.can_read_material(user_id, material))
                else:
                    deny = not (material_service.can_write_material(user_id, material))
            if not deny:
                return f(request, **kwargs)
            else:
                return HttpResponseForbidden()

        return do_filter


def get_auth_service():
    auth_service = user_service_container.load(AuthService.__name__)
    assert isinstance(auth_service, AuthService)
    return auth_service


def get_material_service():
    material_service = lc_service_container.load(MaterialService.__name__)
    assert isinstance(material_service, MaterialService)
    return material_service
