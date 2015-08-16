from commons.db.api.factories import MongoSerializationFactory, MongoDatabaseFactory
from commons.ioc import Provider
from lc.problem.api.daos import ProblemDao
from lc.problem.api.services import ProblemService
from lc.problem.impl.daos import ProblemDaoImpl
from lc.problem.impl.services import ProblemServiceImpl


class ProblemDaoProvider(Provider):
    def register(self, container, containers):
        mongo_container = containers["MongoContainer"]
        mongo_serialization_fac = mongo_container.load(MongoSerializationFactory.__name__)
        mongo_database_factory = mongo_container.load(MongoDatabaseFactory.__name__)
        assert(isinstance(mongo_serialization_fac,MongoSerializationFactory))
        assert(isinstance(mongo_database_factory,MongoDatabaseFactory))
        db = mongo_database_factory.get_db_lc()
        container.save(ProblemDao.__name__, ProblemDaoImpl(mongo_serialization_fac,db))


class ProblemServiceProvider(Provider):
    def register(self, container, containers):
        lc_dao_container = containers["LCDaoContainer"]
        container.save(ProblemService.__name__, ProblemServiceImpl(lc_dao_container.load(ProblemDao.__name__)))
