from commons.ioc import Container
from .config import dao_providers, service_providers


class LCDaoContainer(Container):
    def __init__(self, providers):
        super().__init__(providers,None)


class LCServiceContainer(Container):
    def __init__(self, providers, containers):
        super().__init__(providers, containers)


lc_dao_container = LCDaoContainer(dao_providers)

lc_service_container = LCServiceContainer(service_providers, {
    "LCDaoContainer": lc_dao_container
})
