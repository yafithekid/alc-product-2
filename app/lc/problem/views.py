from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import ProblemForm, MultipleChoiceProblemForm, ShortAnswerProblemForm
from lc.models import Problem


def index(request):
    template = loader.get_template("problem/index.html")
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def create(request):
    type = request.GET.get('type',Problem.MULTIPLE_CHOICE)
    if type == Problem.MULTIPLE_CHOICE:
        Form = MultipleChoiceProblemForm
    else:
        Form = ShortAnswerProblemForm
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse('problem.index'))
    else:
        form = Form
    available_types = {
        'MC' : Problem.MULTIPLE_CHOICE,
        'SA' : Problem.SHORT_ANSWER
    }
    return render(request, "problem/create.html", {'form': form,'type':type,'available_types':available_types})
