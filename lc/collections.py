from app.lc.course.forms import CourseForm
from app.lc.problem.forms import ProblemForm, MultipleChoiceProblemForm, ShortAnswerProblemForm
from commons.db.persistence import Entity
from commons.fields import ObjectIdField, StringField, DocumentField, ChoiceField


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
    creator_id = StringField(required=True)
    type = StringField(required=True, max_length=2)

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


class Course(Entity):
    PUBLIC = "public"
    PRIVATE = "private"

    title = StringField(required=True, max_length=255)
    description = StringField(required=True)
    creator_id = ObjectIdField(required=True)
    type = ChoiceField(required=True, choices=[PUBLIC, PRIVATE])

    @classmethod
    def from_form(cls, form: CourseForm):
        course = cls()
        course.title = form.cleaned_data['title']
        course.description = form.cleaned_data['description']
        course.type = form.cleaned_data['type']
        return course

    @classmethod
    def to_form(cls, course):
        return CourseForm({
            "title": course.title,
            "description": course.description,
            "type": course.type
        })


class Material(Entity):
    title = StringField(required=True, max_length=255)
    content = StringField(required=True)
    creator_id = ObjectIdField(required=True)
