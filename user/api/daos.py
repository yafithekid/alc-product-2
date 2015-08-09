from user.models import User


class UserDao:
    def find_by_email(self,email:str):
        raise NotImplementedError

    def find(self,filter:dict):
        raise NotImplementedError

    def update(self,user:User):
        raise NotImplementedError

    def insert(self,user:User):
        raise NotImplementedError
