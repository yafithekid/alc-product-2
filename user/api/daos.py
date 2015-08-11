from user.collections import User


class UserDao:
    def find_by_email(self, email: str) -> User:
        raise NotImplementedError

    def find_by_id(self, id: str) -> User:
        raise NotImplementedError

    def find(self, _filter: dict):
        raise NotImplementedError

    def update(self, user: User) -> User:
        raise NotImplementedError

    def insert(self, user: User) -> str:
        raise NotImplementedError
