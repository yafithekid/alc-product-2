from user.collections import User


class UserService():
    def find_by_id(self, _id: str) -> User:
        raise NotImplementedError

    def find_by_email(self, email: str) -> User:
        raise NotImplementedError

    def find(self,email: str,password: str) -> User:
        raise NotImplementedError

    def add_user(self, email: str, password: str, name: str) -> str:
        raise NotImplementedError

    def hash_password(self,password: str) -> str:
        raise NotImplementedError

