from django.db import models
import datetime


class User(models.Model):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3

    email = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)
    confirmed = models.BooleanField(default=False)
    roles = models.ManyToManyField('Role')


class PasswordReset(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)


class Confirmation(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)


class Role(models.Model):
    STUDENT = 1,
    TEACHER = 2,
    ADMIN = 3,
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (ADMIN, 'admin')
    )

    id = models.IntegerField(choices=ROLE_CHOICES, primary_key=True)
    name = models.CharField(max_length=255)
