from django import forms


class CourseForm(forms.Form):
    PUBLIC = "public"
    PRIVATE = "private"

    title = forms.CharField(required=True, max_length=255)
    description = forms.CharField(required=True)
    type = forms.CharField(required=True, max_length=255)
