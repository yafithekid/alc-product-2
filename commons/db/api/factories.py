from pymongo import MongoClient
from pymongo.database import Database
from commons.db.api.services import MongoSerialization


class MongoDatabaseFactory:
    def get_db_user(self) -> Database:
        raise NotImplementedError

    def get_db_lc(self) -> Database:
        raise NotImplementedError


class MongoSerializationFactory:
    def get_instance(self) -> MongoSerialization:
        raise NotImplementedError
