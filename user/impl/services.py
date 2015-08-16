from user.api.daos import UserDao
from user.api.services import UserService
from user.collections import User

import hashlib


class UserServiceImpl(UserService):
    def find_by_id(self, _id: str) -> User:
        return self.user_dao.find_by_id(_id)

    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao
        self.add_default_user()

    def hash_password(self, password: str) -> str:
        h = hashlib.sha256()
        h.update(password.encode("utf-8"))
        return h.hexdigest()

    def find_by_email(self, email: str) -> User:
        return self.user_dao.find_by_email(email)

    def find(self, email: str, password: str) -> User:
        return self.user_dao.find({"email": email, "password": self.hash_password(password)})

    def add_user(self, email: str, password: str, name: str, roles: list=None) -> str:
        user = User()
        user.email = email
        user.password = self.hash_password(password)
        user.name = name
        if roles is None:
            user.roles = [User.STUDENT]
        else:
            user.roles = roles
        return self.user_dao.insert(user)

    # TODO HIGH remove this function since it can create security hole
    def add_default_user(self):
        self.add_user("s@s.com", "s", "Dummy Student", [User.STUDENT])
        self.add_user("t@t.com", "t", "Dummy Teacher", [User.TEACHER])
        self.add_user("a@a.com", "a", "Dummy Admin", [User.ADMIN])
