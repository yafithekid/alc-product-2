from user.models import User


class BasicAuthBackend(object):
    def authenticate(self, email = None, password = None):
        return User(email=email, password=password)
