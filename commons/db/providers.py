from commons.db.impl.factories import MongoClientFactoryImpl
from commons.ioc import Provider


class MongoClientFactoryProvider(Provider):
    def __init__(self, default_host):
        self.__default_host = default_host

    def register(self, interface_name, container, containers):
        container.save(interface_name,MongoClientFactoryImpl(self.__default_host))