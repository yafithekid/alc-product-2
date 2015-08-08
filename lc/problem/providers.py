from commons.ioc import Provider
from lc.problem.api.daos import ProblemDao
from lc.problem.api.services import ProblemService
from lc.problem.impl.daos import ProblemDaoImpl
from lc.problem.impl.services import ProblemServiceImpl


class ProblemDaoProvider(Provider):
    def register(self, container, containers):
        container.save(ProblemDao.__name__, ProblemDaoImpl())


class ProblemServiceProvider(Provider):
    def register(self, container, containers):
        lc_dao_container = containers["LCDaoContainer"]
        container.save(ProblemService.__name__, ProblemServiceImpl(lc_dao_container.load(ProblemDao.__name__)))
