from lc.course.providers import CourseServiceProvider, CourseDaoProvider
from lc.material.providers import MaterialDaoProvider, MaterialServiceProvider
from lc.problem.providers import ProblemServiceProvider, ProblemDaoProvider

dao_providers = [
    ProblemDaoProvider(),
    CourseDaoProvider(),
    MaterialDaoProvider()
]

service_providers = [
    ProblemServiceProvider(),
    CourseServiceProvider(),
    MaterialServiceProvider()
]