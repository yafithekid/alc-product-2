from django import forms

class RegisterForm(forms.Form):
  email = forms.EmailField(max_length=200)
  name = forms.CharField(max_length=200)
  password = forms.CharField(widget=forms.PasswordInput,max_length=200)
  confirm_password = forms.CharField(widget=forms.PasswordInput,max_length=200)