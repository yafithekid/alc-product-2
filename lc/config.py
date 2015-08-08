from lc.problem.api.daos import ProblemDao
from lc.problem.providers import ProblemServiceProvider, ProblemDaoProvider
from lc.problem.api.services import ProblemService

dao_providers = [
    ProblemDaoProvider()
]

service_providers = [
    ProblemServiceProvider()
]