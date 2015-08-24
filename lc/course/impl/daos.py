import logging
from bson import ObjectId
from pymongo.database import Database
from commons.db.api.factories import MongoSerializationFactory
from lc.collections import Course
from lc.course.api.daos import CourseDao


class CourseDaoImpl(CourseDao):
    COURSE_COLLECTION_NAME = "course"
    logger = logging.getLogger("lc")

    def __init__(self,
                 mongo_serialization_factory: MongoSerializationFactory,
                 db: Database):
        self.mongo_serialization = mongo_serialization_factory.get_instance()
        self.db = db

    def count(self, query: dict):
        coll = self.get_collection()
        return coll.count(query)

    def find(self, query: dict, sort: list, limit: int, skip: int):
        coll = self.get_collection()
        db_cursor = coll.find(filter=query, sort=sort, limit=limit, skip=skip)
        ret = []
        for db_object in db_cursor:
            ret.append(self.mongo_serialization.to_entity(db_object, Course))
        print("ret")
        print(ret)
        return ret

    def find_by_id(self, _id: str) -> Course:
        coll = self.get_collection()
        try:
            db_object = coll.find_one({"_id": ObjectId(_id)})
            return self.mongo_serialization.to_entity(db_object, Course)
        # TODO should change to mongo exception
        except Exception as e:
            self.logger.error(e)

    def get_collection(self):
        return self.db.get_collection(self.COURSE_COLLECTION_NAME)

    def insert(self, course: Course) -> str:
        coll = self.get_collection()
        try:
            db_object = self.mongo_serialization.to_mongo(course, Course)
            insert_result = coll.insert_one(db_object)
            return str(insert_result.inserted_id)
        # TODO should change to mongo exception
        except Exception as e:
            return None
