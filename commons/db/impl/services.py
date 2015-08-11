from commons.db.api.services import MongoSerialization
from commons.db.persistence import Entity
from commons.fields import Field


class MongoSerializationImpl(MongoSerialization):
    def to_entity(self, objek: dict, clazz) -> Entity:
        entity = clazz()
        if objek is None:
            entity = None
        else:
            for key,value in objek.items():
                setattr(entity, key, value)
        return entity

    def to_mongo(self, objek: Entity, clazz) -> dict:
        objek.validate()
        if objek.has_error():
            print("objek has error")
            raise Exception(objek.errors.__str__())
        ret = {}
        field_names = clazz.get_field_names()
        for field_name in field_names:
            print(field_name)
            field = getattr(objek,field_name)
            if not (isinstance(field,Field)):
                ret[field_name] = getattr(objek, field_name)
        print(ret)
        return ret
