from pymongo import MongoClient
from pymongo.database import Database
from commons.db.api.factories import MongoSerializationFactory, MongoDatabaseFactory
from commons.db.api.services import MongoSerialization
from commons.db.impl.services import MongoSerializationImpl


class MongoDatabaseFactoryImpl(MongoDatabaseFactory):
    def __init__(self, default_host='localhost'):
        self.default_host = default_host

    def get_db_user(self) -> Database:
        return MongoClient(self.default_host,27017).get_database("alc-user")

    def get_db_lc(self) -> Database:
        return MongoClient(self.default_host,27017).get_database("alc-lc")


class MongoSerializationFactoryImpl(MongoSerializationFactory):
    def get_instance(self) -> MongoSerialization:
        return MongoSerializationImpl()
