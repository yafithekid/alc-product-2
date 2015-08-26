from django.http import HttpRequest
from commons.db.data import ResultWithPagination
from lc.collections import Material
from lc.material.api.daos import MaterialDao
from lc.material.api.services import MaterialService
from user.collections import User


class MaterialServiceImpl(MaterialService):
    def edit_material(self, material: Material):
        return self.material_dao.update(material)

    def can_write_material(self, user_id: User, material: Material):
        return material.creator_id == user_id

    def can_read_material(self, user_id: User, material: Material):
        # TODO impl
        return True

    def paginate(self, query: dict, sort: list, limit: int, request: HttpRequest) -> ResultWithPagination:
        return self.material_dao.paginate(query, sort, limit, request)

    def __init__(self,
                 material_dao: MaterialDao):
        self.material_dao = material_dao

    def add_material(self, material: Material) -> str:
        return self.material_dao.insert(material)

    def find_by_id(self, _id: str) -> Material:
        return self.material_dao.find_by_id(_id)
