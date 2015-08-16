from commons.db.persistence import Entity
from commons.fields import StringField, ListField


class User(Entity):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    email = StringField(required=True, max_length=255)
    name = StringField(required=True, max_length=255)
    password = StringField(required=True, max_length=255)
    roles = ListField(required=True)
