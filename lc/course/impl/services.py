from django.http import HttpRequest
from lc.collections import Course
from lc.course.api.daos import CourseDao
from lc.course.api.services import CourseService


class CourseServiceImpl(CourseService):
    def can_read_course(self, user_id: str, course: Course) -> bool:
        #all user can read course
        return True

    def can_write_course(self, user_id: str, course: Course) -> bool:
        return course.creator_id == user_id

    def paginate(self, _filter: dict, sort: list, limit: int, request: HttpRequest):
        return self.course_dao.paginate(_filter, sort, limit, request)

    def __init__(self, course_dao: CourseDao):
        self.course_dao = course_dao

    def add_course(self, course: Course) -> str:
        return self.course_dao.insert(course)

    def find_by_id(self, _id: str) -> Course:
        return self.course_dao.find_by_id(_id)
