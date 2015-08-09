from commons.db.containers import mongo_container
from commons.ioc import Container
from .config import service_providers, dao_providers


class UserDaoContainer(Container):
    def __init__(self, providers,containers):
        super().__init__(providers,containers)


class UserServiceContainer(Container):
    def __init__(self, providers, containers):
        super().__init__(providers, containers)


user_dao_container = UserDaoContainer(dao_providers,{
    "MongoContainer": mongo_container
})

user_service_container = UserServiceContainer(service_providers, {
    "UserDaoContainer": user_dao_container
})
