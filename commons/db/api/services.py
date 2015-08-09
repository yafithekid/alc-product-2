from commons.db.persistence import Entity


class MongoSerialization:
    def to_entity(self, objek: dict,clazz) -> Entity:
        raise NotImplementedError

    def to_mongo(self, object: Entity,clazz) -> dict:
        raise NotImplementedError
