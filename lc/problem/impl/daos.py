import logging
from bson import ObjectId
from pymongo.database import Database
from commons.db.api.factories import MongoSerializationFactory
from lc.collections import Problem
from lc.problem.api.daos import ProblemDao


class ProblemDaoImpl(ProblemDao):
    COLLECTION_NAME = "problem"
    logger = logging.getLogger("lc")

    def find_by_id(self, _id: str) -> Problem:
        try:
            coll = self.get_collection()
            db_object = coll.find_one({"_id": ObjectId(_id)})
            problem =  self.mongo_serialization.to_entity(db_object, Problem)
            return problem
        except Exception as e:
            self.logger.error(e)

    def update(self, problem: Problem):
        pass

    def insert(self, problem: Problem) -> str:
        try:
            coll = self.get_collection()
            db_object = self.mongo_serialization.to_mongo(problem, Problem)
            print(db_object)
            insert_one_result = coll.insert_one(db_object)
            return str(insert_one_result.inserted_id)
        except Exception as e:
            print(e)
            self.logger.error(e)

    def __init__(self,
                 mongo_serialization_factory: MongoSerializationFactory,
                 db: Database
                 ):
        self.mongo_serialization = mongo_serialization_factory.get_instance()
        self.db = db

    def get_collection(self):
        return self.db.get_collection(ProblemDaoImpl.COLLECTION_NAME)
