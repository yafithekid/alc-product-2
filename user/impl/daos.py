from pymongo.database import Database
from commons.db.api.factories import MongoSerializationFactory
from user.api.daos import UserDao
from user.collections import User


class UserDaoImpl(UserDao):
    COLLECTION_NAME = "user"

    def __init__(self,
                 mongo_serialization_factory: MongoSerializationFactory,
                 db: Database
                 ):
        self.mongo_serialization_factory = mongo_serialization_factory
        self.mongo_serialization = self.mongo_serialization_factory.get_instance()
        self.db = db
        print(self.db)
        self.coll = db.get_collection(UserDaoImpl.COLLECTION_NAME)

    def find(self, filters: dict):
        raise NotImplementedError

    def update(self, user: User):
        raise NotImplementedError

    def find_by_email(self, email):
        res = self.coll.find_one({"_id": email})
        return self.mongo_serialization.to_entity(res, User)

    def insert(self, user: User):
        mongo_object = self.mongo_serialization.to_mongo(user,User)
        self.coll.insert_one(mongo_object)
