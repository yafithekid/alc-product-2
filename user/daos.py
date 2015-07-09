from main.mongoconf import CONNECTION
from mongoengine import connect

connect(CONNECTION['default']['name'])
class UserDao:
  @staticmethod
  def insertUser(user):
    user.save()
    return user