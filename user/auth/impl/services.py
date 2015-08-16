from django.contrib.messages.storage import session
from user.api.services import UserService
from user.auth.api.services import AuthService
from user.collections import User


class AuthServiceImpl(AuthService):
    KEY = "auth_user"
    RBAC_ROLES = {
        User.ADMIN: [User.ADMIN, User.TEACHER, User.STUDENT],
        User.TEACHER: [User.TEACHER, User.STUDENT],
        User.STUDENT: [User.STUDENT]
    }

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_value(self, key, _session):
        if _session.has_key(self.KEY):
            _dict = _session[self.KEY]
            if key in _dict:
                return _dict[key]
            else:
                return None
        else:
            return None

    def login(self, user: User, _session: session):
        _session[self.KEY] = {
            "email": user.email,
            "name": user.name,
            "roles": user.roles,
            "_id": str(user._id)
        }

    def logout(self, _session: session):
        if _session.has_key(self.KEY):
            _session[self.KEY] = None

    def attempt(self, email: str, password: str) -> User:
        user = self.user_service.find(email=email, password=password)
        return user

    def is_logged_in(self, _session: session):
        return _session.has_key(self.KEY) and not (_session[self.KEY] is None)

    def is_authorized_for(self, _session: session, min_role: str):
        if not self.is_logged_in(_session):
            return False
        user_roles = _session[self.KEY]["roles"]

        roles_available = []
        for user_role in user_roles:
            roles_available.extend(self.RBAC_ROLES.get(user_role, []))
        if min_role in roles_available:
            return True
        else:
            return False
