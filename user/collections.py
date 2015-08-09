from commons.db.persistence import Entity, StringField


class User(Entity):
    _id = StringField(required=True)
    name = StringField(required=True, max_length=255)
    password = StringField(max_length=255)