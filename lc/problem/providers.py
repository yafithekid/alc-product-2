from commons.ioc import Provider
from lc.problem.api.daos import ProblemDao
from lc.problem.impl.daos import ProblemDaoImpl
from lc.problem.impl.services import ProblemServiceImpl


class DaoProvider(Provider):
    def register(self, interface_name, container, containers):
        container.save(interface_name, ProblemDaoImpl())


class ProblemProvider(Provider):
    def register(self, interface_name, container, containers):
        print(containers)
        lc_dao_container = containers["LCDaoContainer"]
        container.save(interface_name, ProblemServiceImpl(lc_dao_container.load(ProblemDao.__name__)))
