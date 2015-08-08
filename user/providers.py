from commons.ioc import Provider
from user.api.daos import UserDao
from user.api.services import UserService
from user.impl.daos import UserDaoImpl
from user.impl.services import UserServiceImpl


class UserDaoProvider(Provider):
    def register(self,container, containers):
        db_container = containers["DBContainer"]
        container.save(UserDao.__name__, UserDaoImpl())


class UserServiceProvider(Provider):
    def register(self, container, containers):
        user_dao_container = containers["UserDaoContainer"]
        container.save(UserService.__name__, UserServiceImpl(user_dao_container.load(UserDao.__name__)))
