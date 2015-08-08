from user.api.daos import UserDao
from user.models import User


class UserDaoImpl(UserDao):
    def findByEmail(self,email):
        return User(email=email)

    def insert(self,user: User):
        #TODO insert user
        print("insert user...")
        print(user)
        return user

