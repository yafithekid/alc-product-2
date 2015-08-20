from django import forms


class MaterialForm(forms.Form):
    title = forms.CharField(required=True, max_length=255)
    content = forms.CharField(required=True)
