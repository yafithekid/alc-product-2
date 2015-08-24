from commons.db.api.factories import MongoSerializationFactory, MongoDatabaseFactory
from commons.ioc import Provider
from lc.quiz.api.daos import QuizDao
from lc.quiz.api.services import QuizService
from lc.quiz.impl.daos import QuizDaoImpl
from lc.quiz.impl.services import QuizServiceImpl


class QuizDaoProvider(Provider):
    def register(self, container, containers):
        mongo_container = containers["MongoContainer"]
        mongo_serialization_fac = mongo_container.load(MongoSerializationFactory.__name__)
        mongo_database_factory = mongo_container.load(MongoDatabaseFactory.__name__)
        assert (isinstance(mongo_serialization_fac, MongoSerializationFactory))
        assert (isinstance(mongo_database_factory, MongoDatabaseFactory))
        db = mongo_database_factory.get_db_lc()
        container.save(QuizDao.__name__, QuizDaoImpl(mongo_serialization_fac, db))


class QuizServiceProvider(Provider):
    def register(self, container, containers):
        lc_dao_container = containers["LCDaoContainer"]
        container.save(QuizService.__name__, QuizServiceImpl(lc_dao_container.load(QuizDao.__name__)))
