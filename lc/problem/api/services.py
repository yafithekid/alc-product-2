from lc.collections import Problem


class ProblemService:
    def find_by_id(self, _id: str) -> Problem:
        raise NotImplementedError

    def insert(self, problem: Problem) -> str:
        raise NotImplementedError
