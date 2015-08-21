from commons.db.data import DaoWithPagination
from lc.collections import Material


class MaterialDao(DaoWithPagination):
    def count(self, query: dict):
        raise NotImplementedError

    def find(self, query: dict, sort: dict, limit: int, skip: int):
        raise NotImplementedError

    def find_by_id(self, _id: str) -> Material:
        raise NotImplementedError

    def insert(self, material: Material) -> str:
        raise NotImplementedError
