from pymongo.database import Database
from commons.db.api.factories import MongoSerializationFactory
from lc.collections import Quiz
from lc.quiz.api.daos import QuizDao


class QuizDaoImpl(QuizDao):
    QUIZ_COLLECTION_NAME = "quiz"

    def __init__(self,
                 mongo_serialization_factory: MongoSerializationFactory,
                 db: Database):
        self.mongo_serialization = mongo_serialization_factory.get_instance()
        self.db = db

    def insert(self, quiz: Quiz) -> str:
        db_object = self.mongo_serialization.to_mongo(quiz, Quiz)
        coll = self.get_collection()
        insert_result = coll.insert_one(db_object)
        return str(insert_result.inserted_id)

    def get_collection(self):
        return self.db.get_collection(self.QUIZ_COLLECTION_NAME)
