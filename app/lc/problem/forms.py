from django import forms

class ProblemForm(forms.Form):
  title = forms.CharField(max_length=200,required=True)
  description = forms.Textarea()
  answer = forms.CharField(max_length=255,required=True)

class MultipleChoiceProblemForm(ProblemForm):
    choice_a = forms.CharField(max_length=255,required=True)
    choice_b = forms.CharField(max_length=255,required=True)
    choice_c = forms.CharField(max_length=255,required=True)
    choice_d = forms.CharField(max_length=255,required=True)
    choice_e = forms.CharField(max_length=255,required=True)

class ShortAnswerProblemForm(ProblemForm):
    pass


