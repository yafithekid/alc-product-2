from app.lc.problem.forms import ProblemForm, MultipleChoiceProblemForm, ShortAnswerProblemForm
from commons.db.persistence import Entity
from commons.fields import ObjectIdField, StringField, DocumentField


class ProblemChoice(Entity):
    content_a = StringField(required=True)
    content_b = StringField(required=True)
    content_c = StringField(required=True)
    content_d = StringField(required=True)
    content_e = StringField(required=True)

    @classmethod
    def from_multiple_choice_form(cls, form: MultipleChoiceProblemForm):
        problem_choice = cls()
        problem_choice.content_a = form.cleaned_data['content_a']
        problem_choice.content_b = form.cleaned_data['content_b']
        problem_choice.content_c = form.cleaned_data['content_c']
        problem_choice.content_d = form.cleaned_data['content_d']
        problem_choice.content_e = form.cleaned_data['content_e']
        return problem_choice


class Problem(Entity):
    MULTIPLE_CHOICE = "mc"
    SHORT_ANSWER = "sa"

    title = StringField(required=True, max_length=255)
    answer = StringField(required=True, max_length=255)
    question = StringField()
    choices = DocumentField(BaseClass=ProblemChoice)

    @classmethod
    def from_form(cls, form: ProblemForm):
        problem = cls()
        problem.title = form.cleaned_data['title']
        problem.answer = form.cleaned_data['answer']
        problem.question = form.cleaned_data['question']
        return problem

    @classmethod
    def from_multiple_choice_form(cls, form: MultipleChoiceProblemForm):
        problem = cls.from_form(form)
        choice = ProblemChoice.from_multiple_choice_form(form)
        problem.choices = choice
        return problem

    @classmethod
    def from_short_answer_form(cls, form: ShortAnswerProblemForm):
        problem = cls.from_form(form)
        return problem
