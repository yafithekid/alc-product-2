from django.http import HttpResponseNotFound
from django.shortcuts import render
from lc.containers import lc_service_container
from lc.material.api.services import MaterialService
from lc.material.filters import AuthorizedForMaterialView


def update(request, _id):
    return render(request, get_template("update.html"), {})


def read(request, _id):
    material_service = get_material_service()
    material = material_service.find_by_id(_id)
    if material is None:
        return HttpResponseNotFound()
    else:
        return render(request, get_template("read.html"), {"material": material})


def get_material_service():
    material_service = lc_service_container.load(MaterialService.__name__)
    assert (isinstance(material_service, MaterialService))
    return material_service


def get_template(filename):
    return "material/detail/" + filename
