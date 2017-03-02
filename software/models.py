from django.db import models
from django.contrib.auth.models import User


class Catching(models.Model):
    image = models.TextField(null=True)
    comment = models.TextField(null=True)
    like_count = models.IntegerField(default=0)
    is_in_pocket = models.BooleanField(default=False)
    confidence = models.IntegerField(default=0)
    registered_time = models.DateTimeField(auto_now_add=True)
    senior = models.ForeignKey('Senior')
    user = models.ForeignKey('Profile')


class Senior(models.Model):
    name = models.CharField(max_length=15)
    image = models.TextField(null=True)
    student_id = models.IntegerField(null=True)
    like_count = models.IntegerField(default=0)
    caught_count = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User)
    is_freshmen = models.BooleanField(default=True)
    catching_count = models.IntegerField(default=0)


class Chatting(models.Model):
    chat = models.TextField(null=False)
    user = models.ForeignKey('Profile', null=True)
    senior = models.ForeignKey('Senior')


class Like(models.Model):
    user = models.ForeignKey('Profile')
    catching = models.ForeignKey('Catching')