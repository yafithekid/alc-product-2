from django.http import HttpRequest
from lc.collections import Course
from user.collections import User


class CourseService:
    def add_course(self, course: Course) -> str:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Course:
        raise NotImplementedError

    def paginate(self, _filter: dict, sort: list, limit: int, request: HttpRequest):
        raise NotImplementedError

    def can_write_course(self, user_id: str, course: Course) -> bool:
        raise NotImplementedError

    def can_read_course(self,user_id:str, course:Course) -> bool:
        raise NotImplementedError
