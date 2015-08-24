from lc.collections import Quiz
from lc.quiz.api.daos import QuizDao
from lc.quiz.api.services import QuizService


class QuizServiceImpl(QuizService):
    def __init__(self, quiz_dao: QuizDao):
        self.quiz_dao = quiz_dao

    def add_quiz(self, quiz: Quiz):
        return self.quiz_dao.insert(quiz)

    def add_problem(self, quiz_id: str, problem_id: str):
        raise NotImplementedError
