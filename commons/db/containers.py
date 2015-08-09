from commons.config import mongo_providers
from commons.ioc import Container


class MongoContainer(Container):
    def __init__(self, providers):
        super().__init__(providers)

mongo_container = MongoContainer(mongo_providers)
