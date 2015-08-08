from commons.ioc import Provider
from user.api.daos import UserDao
from user.impl.daos import UserDaoImpl
from user.impl.services import UserServiceImpl


class UserDaoProvider(Provider):
    def register(self, interface_name, container, containers):
        db_container = containers["DBContainer"]
        container.save(interface_name, UserDaoImpl())


class UserServiceProvider(Provider):
    def register(self, interface_name, container, containers):
        user_dao_container = containers["UserDaoContainer"]
        container.save(interface_name, UserServiceImpl(user_dao_container.load(UserDao.__name__)))
