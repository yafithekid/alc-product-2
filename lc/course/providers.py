from commons.db.api.factories import MongoSerializationFactory, MongoDatabaseFactory
from commons.ioc import Provider
from lc.course.api.daos import CourseDao
from lc.course.api.services import CourseService
from lc.course.impl.daos import CourseDaoImpl
from lc.course.impl.services import CourseServiceImpl


class CourseDaoProvider(Provider):
    def register(self, container, containers):
        mongo_container = containers["MongoContainer"]
        mongo_serialization_fac = mongo_container.load(MongoSerializationFactory.__name__)
        mongo_database_factory = mongo_container.load(MongoDatabaseFactory.__name__)
        assert (isinstance(mongo_serialization_fac, MongoSerializationFactory))
        assert (isinstance(mongo_database_factory, MongoDatabaseFactory))
        db = mongo_database_factory.get_db_lc()
        container.save(CourseDao.__name__, CourseDaoImpl(mongo_serialization_fac, db))


class CourseServiceProvider(Provider):
    def register(self, container, containers):
        lc_dao_container = containers["LCDaoContainer"]
        course_dao = lc_dao_container.load(CourseDao.__name__)
        assert (course_dao, CourseDao)
        container.save(CourseService.__name__, CourseServiceImpl(course_dao))
