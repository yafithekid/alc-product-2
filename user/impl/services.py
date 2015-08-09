from user.api.daos import UserDao
from user.api.services import UserService
from user.models import User


class UserServiceImpl(UserService):
    def __init__(self,user_dao: UserDao):
        self.user_dao = user_dao

    def findByEmail(self, email: str):
        return self.user_dao.find_by_email(email)

    def addUser(self,email: str,password: str,name: str):
        user = User(email = email,password = password,name = name)
        self.user_dao.insert(user)