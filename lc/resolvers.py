from lc.containers import lc_service_container
from lc.material.api.services import MaterialService
from user.auth.api.services import AuthService
from user.containers import user_service_container


def get_material_service():
    material_service = lc_service_container.load(MaterialService.__name__)
    assert (isinstance(material_service, MaterialService))
    return material_service


def get_auth_service():
    auth_service = user_service_container.load(AuthService.__name__)
    assert (isinstance(auth_service, AuthService))
    return auth_service
