# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('software', '0004_senior_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.TextField(null=True)),
                ('comment', models.TextField(null=True)),
                ('like_count', models.IntegerField(default=0)),
                ('is_succeed', models.BooleanField(default=False)),
                ('registered_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chatting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catching', models.ForeignKey(to='software.Catching')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_freshmen', models.BooleanField(default=True)),
                ('catching_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='senior',
            name='registered_time',
        ),
        migrations.AddField(
            model_name='senior',
            name='caught_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='senior',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='senior',
            name='student_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to='software.Profile'),
        ),
        migrations.AddField(
            model_name='chatting',
            name='senior',
            field=models.ForeignKey(to='software.Senior'),
        ),
        migrations.AddField(
            model_name='chatting',
            name='user',
            field=models.ForeignKey(to='software.Profile', null=True),
        ),
        migrations.AddField(
            model_name='catching',
            name='senior',
            field=models.ForeignKey(to='software.Senior'),
        ),
        migrations.AddField(
            model_name='catching',
            name='user',
            field=models.ForeignKey(to='software.Profile'),
        ),
    ]
