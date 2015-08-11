from django.contrib.messages.storage import session
from user.api.services import UserService
from user.auth.api.services import AuthService
from user.collections import User


class AuthServiceImpl(AuthService):
    KEY = "auth_user"

    def __init__(self,user_service:UserService):
        self.user_service = user_service

    def login(self, user: User, _session: session):
        _session[self.KEY] = {
            "email" : user.email,
            "name" : user.name
        }

    def logout(self,_session:session):
        if _session.has_key(self.KEY):
            _session[self.KEY] = None

    def attempt(self, email: str, password: str) -> User:
        user = self.user_service.find(email=email,password=password)
        return user
