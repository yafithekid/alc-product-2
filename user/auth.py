from user.api.services import UserService
from user.containers import user_service_container

class BasicAuthBackend(object):
    def authenticate(self, email = None, password = None):
        user_service = user_service_container.load(UserService.__name__)
        assert (isinstance(user_service,UserService))
        user = user_service.find(email = email,password = password)
        return user
