from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from app.lc.material.forms import MaterialForm
from lc.collections import Material
from lc.filters import Authorized
from lc.material.filters import MaterialAuthorization
from lc.resolvers import get_material_service, get_auth_service


@MaterialAuthorization(min_level=MaterialAuthorization.WRITE)
def update(request, _id):
    material_service = get_material_service()
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = material_service.find_by_id(_id)
            material.title = form.cleaned_data['title']
            material.content = form.cleaned_data['content']
            material_service.edit_material(material)
            return HttpResponseRedirect(reverse("material.read", args=[_id]))
    else:
        material = material_service.find_by_id(_id)
        form = Material.to_form(material)
    return render(request, get_template("update.html"), {"form": form, "id": _id})


@Authorized()
def read(request, _id):
    material_service = get_material_service()
    material = material_service.find_by_id(_id)
    if material is None:
        return HttpResponseNotFound()
    else:
        auth_service = get_auth_service()
        user_id = auth_service.get_value("_id", request.session)
        can_edit = material_service.can_write_material(user_id, material)
        return render(request, get_template("read.html"), {"material": material, "can_edit": can_edit,"id":_id})


def get_template(filename):
    return "material/detail/" + filename
