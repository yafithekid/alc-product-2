from django.contrib.auth.models import User
from commons.db.persistence import Entity, StringField


class User(Entity,User):
    email = StringField(required=True, max_length=255)
    name = StringField(required=True, max_length=255)
    password = StringField(max_length=255)


    # django user authentication
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass
