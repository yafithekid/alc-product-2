from lc.collections import Problem
from lc.problem.api.daos import ProblemDao
from lc.problem.api.services import ProblemService


class ProblemServiceImpl(ProblemService):
    def find_by_id(self, _id: str) -> Problem:
        return self.problem_dao.find_by_id(_id)

    def __init__(self, problem_dao: ProblemDao):
        self.problem_dao = problem_dao

    def insert(self, problem: Problem) -> str:
        return self.problem_dao.insert(problem)
