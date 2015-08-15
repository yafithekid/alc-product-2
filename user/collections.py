from commons.db.persistence import Entity, StringField
from commons.fields import ObjectIdField


class User(Entity):
    _id = ObjectIdField()
    email = StringField(required=True, max_length=255)
    name = StringField(required=True, max_length=255)
    password = StringField(max_length=255)

