# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('slug', models.SlugField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemType',
            fields=[
                ('id', models.CharField(max_length=b'2', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, choices=[((1,), b'student'), ((2,), b'teacher'), ((3,), b'admin')])),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(default=b'MAT_SMA', max_length=6, serialize=False, primary_key=True, choices=[(b'MAT_SMA', b'matematika sma'), (b'FIS_SMA', b'fisika sma'), (b'KIM_SMA', b'kimia sma'), (b'BIO_SMA', b'biologi sma'), (b'GEO_SMA', b'geografi sma'), (b'KOM_SMA', b'komputer sma'), (b'AST_SMA', b'astronomi sma'), (b'EKO_SMA', b'ekonomi sma'), (b'BUM_SMA', b'kebumian sma')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('role', models.ForeignKey(to='lc.Role')),
                ('user', models.ForeignKey(to='lc.User')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='lc.Role', through='lc.UserRole'),
        ),
        migrations.AddField(
            model_name='problem',
            name='problem_type',
            field=models.ForeignKey(default=b'SA', to='lc.ProblemType'),
        ),
        migrations.AddField(
            model_name='problem',
            name='subject',
            field=models.ForeignKey(to='lc.Subject'),
        ),
        migrations.AddField(
            model_name='problem',
            name='user',
            field=models.ForeignKey(to='lc.User'),
        ),
    ]
