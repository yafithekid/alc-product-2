import logging
from bson import ObjectId
from pymongo.database import Database
from commons.db.api.factories import MongoSerializationFactory
from lc.collections import Material
from lc.material.api.daos import MaterialDao


class MaterialDaoImpl(MaterialDao):
    MATERIAL_COLLECTION_NAME = "material"
    logger = logging.getLogger("lc")

    def __init__(self,
                 mongo_serialization_factory: MongoSerializationFactory,
                 db: Database
                 ):
        self.mongo_serialization = mongo_serialization_factory.get_instance()
        self.db = db

    def insert(self, material: Material) -> str:
        coll = self.get_collection()
        db_object = self.mongo_serialization.to_mongo(material, Material)
        try:
            insert_object = coll.insert_one(db_object)
            return insert_object.inserted_id
        # TODO more specific exception
        except Exception as e:
            self.logger.error(self.__class__.__name__ + ":" + e.args)
            return None

    def find_by_id(self, _id: str) -> Material:
        coll = self.get_collection()

        try:
            db_object = coll.find_one({"_id": ObjectId(_id)})
            material = self.mongo_serialization.to_entity(db_object, Material)
            return material
        # TODO more specific exeption
        except Exception as e:
            print(e)
            self.logger.error(e.args)
            return None

    def get_collection(self):
        return self.db.get_collection(self.MATERIAL_COLLECTION_NAME)

    def find(self, query: dict, sort: dict, limit: int, skip: int):
        print("here")
        retval = []
        coll = self.get_collection()
        try:
            db_results = coll.find(filter=query, sort=sort, limit=limit, skip=skip)
            for db_object in db_results:
                retval.append(self.mongo_serialization.to_entity(db_object, Material))
            return retval
        # TODO more specific exception
        except Exception as e:
            print(e)
            self.logger.error(e.args)

    def count(self, query: dict):
        coll = self.get_collection()
        return coll.count(query)
