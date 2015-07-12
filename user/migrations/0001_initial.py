# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('email', models.CharField(primary_key=True, max_length=255, serialize=False)),
                ('token', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('email', models.CharField(primary_key=True, max_length=255, serialize=False)),
                ('token', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(primary_key=True, choices=[((1,), 'student'), ((2,), 'teacher'), ((3,), 'admin')], serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('confirmed', models.BooleanField(default=False)),
                ('roles', models.ManyToManyField(to='user.Role')),
            ],
        ),
    ]
