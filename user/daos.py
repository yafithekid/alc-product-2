from user.models import User

class UserDao:
  @staticmethod
  def insert(user: User):
    user.save()
    return user

  @staticmethod
  def findById(id: str):
    return User.objects.filter(id__exact=id).first()