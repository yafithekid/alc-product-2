from lc.collections import Quiz


class QuizService:
    def add_quiz(self, quiz: Quiz):
        raise NotImplementedError

    def add_problem(self, quiz_id: str, problem_id: str):
        raise NotImplementedError
