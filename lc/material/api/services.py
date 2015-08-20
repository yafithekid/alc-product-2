from django.http import HttpRequest
from commons.db.data import ResultWithPagination
from lc.collections import Material


class MaterialService:
    def find_by_id(self,_id:str) -> Material:
        raise NotImplementedError

    def add_material(self,material:Material) -> str:
        raise NotImplementedError

    def paginate(self, query: dict, sort: dict, limit: int, request: HttpRequest) -> ResultWithPagination:
        raise NotImplementedError