from commons.ioc import Container
from .config import dao_providers, service_providers
from commons.db.containers import mongo_container


class LCDaoContainer(Container):
    def __init__(self, providers, containers):
        super().__init__(providers, containers)


class LCServiceContainer(Container):
    def __init__(self, providers, containers):
        super().__init__(providers, containers)


lc_dao_container = LCDaoContainer(dao_providers, {
    "MongoContainer": mongo_container
})

lc_service_container = LCServiceContainer(service_providers, {
    "LCDaoContainer": lc_dao_container
})
