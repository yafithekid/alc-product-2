from django.http import HttpRequest
from lc.containers import lc_service_container
from lc.material.api.services import MaterialService


class AuthorizedForMaterialView(object):
    def __call__(self, f):
        def do_filter(request: HttpRequest, **kwargs):
            material_service = get_material_service()
            material = material_service.find_by_id(kwargs["_id"])
            # TODO impl
            return f(request, **kwargs)

        return do_filter


def get_material_service():
    material_service = lc_service_container.load(MaterialService.__name__)
    assert isinstance(material_service, MaterialService)
    return material_service
