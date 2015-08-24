from django.shortcuts import render


# Create your views here.
from lc.containers import lc_service_container
from lc.quiz.api.services import QuizService


def index(request):
    quiz_service = get_quiz_service()
    return render(request, get_template("index.html"), {})


def create(request):
    quiz_service = get_quiz_service()
    return render(request, get_template("create.html"), {})


def get_template(filename):
    return "quiz/" + filename


def get_quiz_service():
    quiz_service = lc_service_container.load(QuizService.__name__)
    assert (isinstance(quiz_service, QuizService))
    return quiz_service
