from django import forms


class ProblemForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    answer = forms.CharField(max_length=255, required=True)
    question = forms.CharField()


class MultipleChoiceProblemForm(ProblemForm):
    content_a = forms.CharField(max_length=255, required=True)
    content_b = forms.CharField(max_length=255, required=True)
    content_c = forms.CharField(max_length=255, required=True)
    content_d = forms.CharField(max_length=255, required=True)
    content_e = forms.CharField(max_length=255, required=True)


class ShortAnswerProblemForm(ProblemForm):
    pass
