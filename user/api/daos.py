from user.models import User


class UserDao():
    def findByEmail(self,email:str):
        raise NotImplementedError

    def insert(self,user:User):
        raise NotImplementedError
