from lc.collections import Course


class CourseService:
    def add_course(self, course: Course) -> str:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Course:
        raise NotImplementedError
