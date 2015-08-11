from django.contrib.messages.storage import session
from user.collections import User


class AuthService:
    def attempt(self,email: str,password:str) -> User:
        raise NotImplementedError

    def login(self,user: User,_session:session):
        raise NotImplementedError

    def logout(self,_session:session):
        raise NotImplementedError