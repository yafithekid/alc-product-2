from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import MultipleChoiceProblemForm, ShortAnswerProblemForm
from lc.collections import Problem
from lc.containers import lc_service_container
from lc.filters import Authorized
from lc.problem.api.services import ProblemService
from user.collections import User


def index(request):
    template = loader.get_template("problem/index.html")
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


@Authorized(min_role=User.TEACHER)
def create(request):
    type = request.GET.get('type', Problem.MULTIPLE_CHOICE)
    if type == Problem.MULTIPLE_CHOICE:
        Form = MultipleChoiceProblemForm
    else:
        Form = ShortAnswerProblemForm
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            if type == Problem.MULTIPLE_CHOICE:
                problem = Problem.from_multiple_choice_form(form)
            else:
                problem = Problem.from_short_answer_form(form)
            problem_service = lc_service_container.load(ProblemService.__name__)
            assert isinstance(problem_service, ProblemService)
            problem_id = problem_service.insert(problem)
            return HttpResponseRedirect(reverse('problem.read', args=[problem_id]))
    else:
        form = Form()
    available_types = {
        'MC': Problem.MULTIPLE_CHOICE,
        'SA': Problem.SHORT_ANSWER
    }
    return render(request, "problem/create.html", {'form': form, 'type': type, 'available_types': available_types})
