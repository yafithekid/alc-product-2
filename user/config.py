from user.api.daos import UserDao
from user.api.services import UserService
from user.providers import UserDaoProvider, UserServiceProvider

dao_providers = {
    UserDao.__name__ : UserDaoProvider()
}

service_providers = {
    UserService.__name__ : UserServiceProvider()
}