from .daos import UserDao
from .models import User

import hashlib

# class for user confirmation
class ConfirmationService:
  @staticmethod
  def sendConfirmationEmail(email:str): pass

class PasswordResetService:
  @staticmethod
  def sendPasswordResetEmail(email:str): pass
    
class UserService:
  @staticmethod
  def validPassword(password,user):
    #_password = (hashlib.sha256(password.encode('utf-8')).digest()).decode('utf-8')
    _password = password
    return _password == user.password
  
  @staticmethod
  def findById(id:str):
    return UserDao.findById(id=id)

  @staticmethod
  def findByEmail(email:str):
    return User.objects.filter(email__exact=email).first()

  @staticmethod
  def addUser(email,password,name):
    #_password = (hashlib.sha256(password.encode('utf-8')).digest()).decode('utf-8')
    _password = password
    user = User(email = email,password = _password,name= name)
    print(user.password)
    UserDao.insert(user)
