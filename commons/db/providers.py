from commons.db.api.factories import MongoDatabaseFactory, MongoSerializationFactory
from commons.db.impl.factories import MongoDatabaseFactoryImpl, MongoSerializationFactoryImpl
from commons.ioc import Provider


class MongoSerializationFactoryProvider(Provider):
    def register(self, container, containers):
        container.save(MongoSerializationFactory.__name__, MongoSerializationFactoryImpl())


class MongoDatabaseFactoryProvider(Provider):
    def __init__(self, default_host):
        self.__default_host = default_host

    def register(self, container, containers):
        container.save(MongoDatabaseFactory.__name__, MongoDatabaseFactoryImpl(self.__default_host))
