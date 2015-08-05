from lc.problem.api.daos import ProblemDao
from lc.problem.providers import ProblemProvider, DaoProvider
from lc.problem.api.services import ProblemService

dao_providers = {
    ProblemDao.__name__ : DaoProvider()
}

service_providers = {
    ProblemService.__name__ : ProblemProvider()
}