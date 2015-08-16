from commons.db.api.services import MongoSerialization
from commons.db.persistence import Entity
from commons.fields import Field, DocumentField


class MongoSerializationImpl(MongoSerialization):
    def to_entity(self, objek: dict, clazz) -> Entity:
        entity = clazz()
        if objek is None:
            entity = None
        else:
            for key, value in objek.items():
                setattr(entity, key, value)
        return entity

    def to_mongo(self, objek: Entity, clazz) -> dict:
        objek.validate()
        if objek.has_error():
            raise Exception(objek.errors.__str__())
        ret = {}
        field_names = clazz.get_field_names()
        for field_name in field_names:
            field = getattr(objek, field_name)
            class_field = getattr(clazz, field_name)
            if not (isinstance(field, Field)):
                if not (isinstance(class_field, DocumentField)):
                    ret[field_name] = field
                else:
                    ret[field_name] = self.to_mongo(field, class_field.BaseClass)
            else:
                ret[field_name] = None
        print(ret)
        return ret
