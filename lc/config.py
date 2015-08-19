from lc.course.providers import CourseServiceProvider, CourseDaoProvider
from lc.problem.providers import ProblemServiceProvider, ProblemDaoProvider

dao_providers = [
    ProblemDaoProvider(),
    CourseDaoProvider()
]

service_providers = [
    ProblemServiceProvider(),
    CourseServiceProvider()
]