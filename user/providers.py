from commons.db.api.factories import MongoSerializationFactory, MongoDatabaseFactory
from commons.ioc import Provider
from user.api.daos import UserDao
from user.api.services import UserService
from user.auth.api.services import AuthService
from user.auth.impl.services import AuthServiceImpl
from user.impl.daos import UserDaoImpl
from user.impl.services import UserServiceImpl


class UserDaoProvider(Provider):
    def register(self,container, containers):
        mongo_container = containers["MongoContainer"]
        mongo_serialization_fac = mongo_container.load(MongoSerializationFactory.__name__)
        mongo_database_factory = mongo_container.load(MongoDatabaseFactory.__name__)
        assert (isinstance(mongo_serialization_fac,MongoSerializationFactory))
        assert (isinstance(mongo_database_factory,MongoDatabaseFactory))
        container.save(UserDao.__name__, UserDaoImpl(
            db=mongo_database_factory.get_db_user(),
            mongo_serialization_factory=mongo_serialization_fac)
        )


class UserServiceProvider(Provider):
    def register(self, container, containers):
        user_dao_container = containers["UserDaoContainer"]
        container.save(UserService.__name__, UserServiceImpl(user_dao_container.load(UserDao.__name__)))

class AuthServiceProvider(Provider):
    def register(self,container, containers):
        user_service = container.load(UserService.__name__)
        container.save(AuthService.__name__,AuthServiceImpl(user_service))
