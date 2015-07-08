from django.db import models
from mongoengine import *
from alc.mongoconf import *
import datetime
# Create your models here.
connect(CONNECTION['default']['NAME'])
# class User(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	email = models.CharField(max_length=255)
# 	name = models.CharField(max_length=255)
# 	password = models.CharField(max_length=255)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)

# 	roles = models.ManyToManyField('Role',through='UserRole')
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

class Problem(Document):
	MULTIPLE_CHOICE = 'MC'
	SHORT_ANSWER = 'SA'
	TYPES = (MULTIPLE_CHOICE,'Multiple Choice',SHORT_ANSWER,'Short Answer')
	
	slug = StringField(max_length=255,unique=True)
	title = StringField(max_length=255,required=True)
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)
	description = StringField()
	author = ReferenceField(User)
	problem_type = StringField(max_length=2,default=MULTIPLE_CHOICE,choices=TYPES)
	subject = ReferenceField('Subject')

class Subject(Document):
	MATEMATIKA_SMA = 'MAT_SMA'
	FISIKA_SMA = 'FIS_SMA'
	KIMIA_SMA = 'KIM_SMA'
	BIOLOGI_SMA = 'BIO_SMA'
	GEOGRAFI_SMA = 'GEO_SMA'
	KOMPUTER_SMA = 'KOM_SMA'
	ASTRONOMI_SMA = 'AST_SMA'
	EKONOMI_SMA = 'EKO_SMA'
	KEBUMIAN_SMA = 'BUM_SMA'
	SUBJECTS = (
		(MATEMATIKA_SMA,'matematika sma'),
		(FISIKA_SMA,'fisika sma'),
		(KIMIA_SMA,'kimia sma'),
		(BIOLOGI_SMA,'biologi sma'),
		(GEOGRAFI_SMA,'geografi sma'),
		(KOMPUTER_SMA,'komputer sma'),
		(ASTRONOMI_SMA,'astronomi sma'),
		(EKONOMI_SMA,'ekonomi sma'),
		(KEBUMIAN_SMA,'kebumian sma')
	)

	_id = StringField(max_length=6,primary_key=True,choices=SUBJECTS)
	name = StringField(max_length=255)
