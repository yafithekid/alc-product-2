from lc.problem.api.daos import ProblemDao


class ProblemDaoImpl(ProblemDao):
    def __init__(self):
        print("Ctor Problem Dao Impl")
