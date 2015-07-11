from user.services import UserService
from commons.commands import Command
from mail.services import MailService
from django.contrib.auth import login

class SendConfirmationEmail(Command):
  def __init__(self,email,token):
    self._email = email
    self._token = token

  def handle(self):
    mail = ConfirmationEmail(self._email,self._token)
    MailService.sendMail()

class RegisterUser(Command):
  def __init__(self,email,password,name):
    self._email = email
    self._password = password
    self._name = name

  def handle(self):
    UserService.addUser(self._email,self._password,self._name)

class LoginUser(Command):
  def __init__(self,email,request):
    self._email = email
    self._request = request

  def handle(self):
    user = UserService.findByEmail(self._email)
    login(self._request,user)