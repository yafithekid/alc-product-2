from django.contrib.messages.storage import session
from user.collections import User


class AuthService:
    def attempt(self, email: str, password: str) -> User:
        raise NotImplementedError

    def login(self, user: User, _session: session):
        raise NotImplementedError

    def logout(self, _session: session):
        raise NotImplementedError

    def is_logged_in(self, _session: session):
        raise NotImplementedError

    def is_authorized_for(self, _session: session, min_role: str):
        raise NotImplementedError

    def get_value(self, key, _session: session):
        raise NotImplementedError
