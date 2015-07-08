from django.db import models



# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	roles = models.ManyToManyField('Role',through='UserRole')


class Subject(models.Model):
	MATEMATIKA_SMA = 'MAT_SMA'
	FISIKA_SMA = 'FIS_SMA'
	KIMIA_SMA = 'KIM_SMA'
	BIOLOGI_SMA = 'BIO_SMA'
	GEOGRAFI_SMA = 'GEO_SMA'
	KOMPUTER_SMA = 'KOM_SMA'
	ASTRONOMI_SMA = 'AST_SMA'
	EKONOMI_SMA = 'EKO_SMA'
	KEBUMIAN_SMA = 'BUM_SMA'
	SUBJECT_CHOICES = (
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
	id = models.CharField(max_length=6,choices=SUBJECT_CHOICES,default=MATEMATIKA_SMA,primary_key=True)

class Role(models.Model):
	STUDENT = 1,
	TEACHER = 2,
	ADMIN = 3,
	ROLE_CHOICES = (
		(STUDENT,'student'),
		(TEACHER,'teacher'),
		(ADMIN,'admin')
	)

	id = models.IntegerField(choices=ROLE_CHOICES,primary_key=True)
	
	

# dibuat supaya jelas aja. sebenarnya gak perlu
class UserRole(models.Model):
	user = models.ForeignKey(User)
	role = models.ForeignKey(Role)
	id = models.AutoField(primary_key=True)

class Problem(models.Model):
	id = models.AutoField(primary_key=True)
	MULTIPLE_CHOICE = 'MC'
	SHORT_ANSWER = 'SA'
	slug = models.SlugField(max_length=255)
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	description = models.TextField(null=True)
	user = models.ForeignKey(User)
	subject = models.ForeignKey(Subject)
	problem_type = models.ForeignKey('ProblemType',default=SHORT_ANSWER)

class ProblemType(models.Model):
	id = models.CharField(max_length='2',primary_key=True)
	name  = models.CharField(max_length=255)

