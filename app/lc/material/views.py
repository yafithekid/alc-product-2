from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.lc.material.forms import MaterialForm
from lc.collections import Material
from lc.containers import lc_service_container
from lc.filters import Authorized
from lc.material.api.services import MaterialService
from user.auth.api.services import AuthService
from user.collections import User
from user.containers import user_service_container


@Authorized(min_role=User.TEACHER)
def create(request):
    form = MaterialForm()
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = Material.from_form(form)
            auth_service = get_auth_service()
            material_service = get_material_service()
            material.creator_id = auth_service.get_value("_id", request.session)
            inserted_id = material_service.add_material(material)
            if not (inserted_id is None):
                return HttpResponseRedirect(reverse("material.read", args=[inserted_id]))
    return render(request, get_template("create.html"), {"form": form})


def update(request):
    return render(request, get_template("update.html"), {})


def index(request):
    return render(request, get_template("index.html"), {})


def read(request, _id):
    return render(request, get_template("read.html"), {})


def get_template(file_name):
    return "material/" + file_name


def get_auth_service():
    auth_service = user_service_container.load(AuthService.__name__)
    assert (isinstance(auth_service, AuthService))
    return auth_service


def get_material_service():
    material_service = lc_service_container.load(MaterialService.__name__)
    assert (isinstance(material_service, MaterialService))
    return material_service
