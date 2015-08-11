from lc.problem.api.daos import ProblemDao
from lc.problem.api.services import ProblemService


class ProblemServiceImpl(ProblemService):

    def find_by_id(self, id: int):
        print("Finding problem with id = "+ id)

    def __init__(self,problem_dao: ProblemDao):
        print("Problem Service Impl")
        self.__problem_dao = problem_dao