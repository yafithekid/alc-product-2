from commons.db.api.factories import MongoSerializationFactory, MongoDatabaseFactory
from commons.ioc import Provider
from lc.material.api.daos import MaterialDao
from lc.material.api.services import MaterialService
from lc.material.impl.daos import MaterialDaoImpl
from lc.material.impl.services import MaterialServiceImpl


class MaterialDaoProvider(Provider):
    def register(self, container, containers):
        mongo_container = containers["MongoContainer"]
        mongo_serialization_fac = mongo_container.load(MongoSerializationFactory.__name__)
        mongo_database_factory = mongo_container.load(MongoDatabaseFactory.__name__)
        assert (isinstance(mongo_serialization_fac, MongoSerializationFactory))
        assert (isinstance(mongo_database_factory, MongoDatabaseFactory))
        db = mongo_database_factory.get_db_lc()
        container.save(MaterialDao.__name__, MaterialDaoImpl(mongo_serialization_fac, db))


class MaterialServiceProvider(Provider):
    def register(self, container, containers):
        lc_dao_container = containers["LCDaoContainer"]
        material_dao = lc_dao_container.load(MaterialDao.__name__)
        assert (material_dao, MaterialDao)
        container.save(MaterialService.__name__, MaterialServiceImpl(material_dao))
