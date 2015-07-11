from main.mongoconf import CONNECTION
from mongoengine import connect
from user.models import User

connect(CONNECTION['default']['name'])

class UserDao:
  @staticmethod
  def insert(user: User):
    user.save()
    return user

  @staticmethod
  def findById(id: str):
    return User.objects(id=id).first()