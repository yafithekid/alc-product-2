from .daos import UserDao
from .models import User

class UserService:
  @staticmethod
  def register(email,password,name):
    user = User(email=email,name=name,password=password)
    return UserDao.insertUser(user)

  @staticmethod
  def findById(id):
    return User.objects(id=id).first()
