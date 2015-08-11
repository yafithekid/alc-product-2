from bson import ObjectId
import pymongo
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
        self.coll = db.get_collection(UserDaoImpl.COLLECTION_NAME)
        self.create_index()

    def find_by_id(self, _id: str) -> User:
        result = self.coll.find_one(ObjectId(_id))
        return self.mongo_serialization.to_entity(result,User)

    def find(self, _filters: dict):
        result = self.coll.find_one(_filters)
        print(_filters)
        return self.mongo_serialization.to_entity(result,User)

    def update(self, user: User) -> User:
        raise NotImplementedError

    def find_by_email(self, email) -> User:
        res = self.coll.find_one({"email": email})
        return self.mongo_serialization.to_entity(res, User)

    def insert(self, user: User) -> str:
        mongo_object = self.mongo_serialization.to_mongo(user, User)
        write_result = self.coll.insert_one(mongo_object)
        return str(write_result.inserted_id)

    def create_index(self):
        self.coll.create_index([("email",pymongo.ASCENDING)], background= True, unique = True)
