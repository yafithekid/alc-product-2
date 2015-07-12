# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
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
                ('id', models.CharField(max_length='2', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(default='MAT_SMA', max_length=6, serialize=False, choices=[('MAT_SMA', 'matematika sma'), ('FIS_SMA', 'fisika sma'), ('KIM_SMA', 'kimia sma'), ('BIO_SMA', 'biologi sma'), ('GEO_SMA', 'geografi sma'), ('KOM_SMA', 'komputer sma'), ('AST_SMA', 'astronomi sma'), ('EKO_SMA', 'ekonomi sma'), ('BUM_SMA', 'kebumian sma')], primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='problem_type',
            field=models.ForeignKey(default='SA', to='lc.ProblemType'),
        ),
        migrations.AddField(
            model_name='problem',
            name='subject',
            field=models.ForeignKey(to='lc.Subject'),
        ),
        migrations.AddField(
            model_name='problem',
            name='user',
            field=models.ForeignKey(to='user.User'),
        ),
    ]
