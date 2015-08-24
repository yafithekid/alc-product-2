from commons.db.data import DaoWithPagination
from lc.collections import Problem


class ProblemDao(DaoWithPagination):
    def count(self, query: dict):
        raise NotImplementedError

    def find(self, query: dict, sort: list, limit: int, skip: int):
        raise NotImplementedError

    def find_by_id(self, _id: str) -> Problem:
        raise NotImplementedError

    def insert(self,problem: Problem) -> str:
        raise NotImplementedError

    def update(self,problem: Problem):
        raise NotImplementedError
