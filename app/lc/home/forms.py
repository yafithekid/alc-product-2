from django import forms
from user.services import UserService

class LoginForm(forms.Form):
  email = forms.EmailField(max_length=200)
  password = forms.CharField(widget=forms.PasswordInput,max_length=200)

  def invalidEmail(self):
    self._errors['email'] = 'Invalid email'

  def invalidPassword(self):
    self._errors['password'] = 'invalid password'

  

class RegisterForm(forms.Form):
  email = forms.EmailField(max_length=200)
  name = forms.CharField(max_length=200)
  password = forms.CharField(widget=forms.PasswordInput,max_length=200)
  confirm_password = forms.CharField(widget=forms.PasswordInput,max_length=200)

  def clean_email(self):
    email = self.cleaned_data.get('email')
    user = UserService.findByEmail(email)
    if (user != None):
      raise forms.ValidationError(u'Email address already exists')
    return email
      
