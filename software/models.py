from django.db import models

class Catching(models.Model):
    image = models.TextField(null=True)
    comment = models.TextField(null=True)
    like_count = models.IntegerField(default=0)
    is_succeed = models.BooleanField(default=False)
    registered_time = models.DateTimeField(auto_now_add=True)
    senior = models.ForeignKey('Senior')
    user = models.ForeignKey('User')

class Senior(models.Model):
	name = models.CharField(max_length=10)
	image = models.TextField(null=True)
	student_id = models.IntegerField(null=True)
	like_count = models.IntegerField(default=0)

class User(models.Model):
	name = models.CharField(max_length=10)
	login_id = models.IntegerField(null=False)
	login_pwd = models.CharField(max_length=10)
	is_freshmen = models.BooleanField(default=True)
	catching_count = models.IntegerField(default=0)
	senior = models.ForeignKey('Senior')

class Chatting(models.Model):
	chat = models.TextField(null=False)
	user = models.ForeignKey('User', null=True)
	senior = models.ForeignKey('Senior')

class Like(models.Model):
	user = models.ForeignKey('User')
	catching = models.ForeignKey('Catching')