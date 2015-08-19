from lc.collections import Course


class CourseDao:
    def find_by_id(self,_id:str) -> Course:
        raise NotImplementedError

    def insert(self,course : Course) -> str:
        raise NotImplementedError
