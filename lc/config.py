from lc.course.providers import CourseServiceProvider, CourseDaoProvider
from lc.material.providers import MaterialDaoProvider, MaterialServiceProvider
from lc.problem.providers import ProblemServiceProvider, ProblemDaoProvider
from lc.quiz.providers import QuizServiceProvider, QuizDaoProvider

dao_providers = [
    ProblemDaoProvider(),
    CourseDaoProvider(),
    MaterialDaoProvider(),
    QuizDaoProvider()
]

service_providers = [
    ProblemServiceProvider(),
    CourseServiceProvider(),
    MaterialServiceProvider(),
    QuizServiceProvider()
]