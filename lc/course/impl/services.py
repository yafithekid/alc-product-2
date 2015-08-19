from lc.collections import Course
from lc.course.api.daos import CourseDao
from lc.course.api.services import CourseService


class CourseServiceImpl(CourseService):
    def __init__(self,course_dao: CourseDao):
        self.course_dao = course_dao

    def add_course(self, course: Course) -> str:
        return self.course_dao.insert(course)

    def find_by_id(self, _id: str) -> Course:
        return self.course_dao.find_by_id(_id)