from mongoengine import *
import datetime

class User(Document):
  STUDENT = 1
  TEACHER = 2
  ADMIN = 3

  email = EmailField(required=True)
  name = StringField(max_length=255)
  password = StringField(max_length=255)
  created_at = DateTimeField(default=datetime.datetime.now)
  updated_at = DateTimeField(default=datetime.datetime.now)
  roles = ListField()