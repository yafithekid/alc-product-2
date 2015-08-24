from commons.db.data import DaoWithPagination
from lc.collections import Course


class CourseDao(DaoWithPagination):
    def count(self, query: dict):
        raise NotImplementedError

    def find(self, query: dict, sort: list, limit: int, skip: int):
        raise NotImplementedError

    def find_by_id(self,_id:str) -> Course:
        raise NotImplementedError

    def insert(self,course : Course) -> str:
        raise NotImplementedError


