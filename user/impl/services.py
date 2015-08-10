from user.api.daos import UserDao
from user.api.services import UserService
from user.collections import User

import hashlib


class UserServiceImpl(UserService):
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    def hash_password(self, password: str) -> str:
        h = hashlib.sha256()
        h.update(password.encode("utf-8"))
        return (h.hexdigest())

    def find_by_email(self, email: str) -> User:
        return self.user_dao.find_by_email(email)

    def find(self,email: str,password: str) -> User:
        return self.user_dao.find({"email":email,password:self.hash_password(password)})

    def add_user(self, email: str, password: str, name: str) -> User:
        user = User()
        user._id=email
        user.password=self.hash_password(password)
        user.name=name

        self.user_dao.insert(user)
        return user
