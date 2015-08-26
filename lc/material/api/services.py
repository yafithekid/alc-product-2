from django.http import HttpRequest
from commons.db.data import ResultWithPagination
from lc.collections import Material
from user.collections import User


class MaterialService:
    def find_by_id(self, _id: str) -> Material:
        raise NotImplementedError

    def add_material(self, material: Material) -> str:
        raise NotImplementedError

    def edit_material(self,material:Material):
        raise NotImplementedError

    def paginate(self, query: dict, sort: list, limit: int, request: HttpRequest) -> ResultWithPagination:
        raise NotImplementedError

    def can_write_material(self, user_id: User, material: Material):
        raise NotImplementedError

    def can_read_material(self, user_id: User, material: Material):
        raise NotImplementedError
