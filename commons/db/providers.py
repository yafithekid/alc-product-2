from commons.db.api.factories import MongoClientFactory
from commons.db.impl.factories import MongoClientFactoryImpl
from commons.ioc import Provider


class MongoClientFactoryProvider(Provider):
    def __init__(self, default_host):
        self.__default_host = default_host

    def register(self, container, containers):
        container.save(MongoClientFactory.__name__,MongoClientFactoryImpl(self.__default_host))