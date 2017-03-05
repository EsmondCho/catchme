from django.db import models
from django.contrib.auth.models import User


class Catching(models.Model):
    image = models.ImageField(upload_to='catching_image/', null=True)
    comment = models.TextField(null=True)
    like_count = models.IntegerField(default=0)
    chatting_count = models.IntegerField(default=0)
    is_in_pocket = models.BooleanField(default=False)
    confidence = models.IntegerField(default=0)
    registered_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True, blank=True, null=True)
    senior = models.ForeignKey('Senior', null=True)
    profile = models.ForeignKey('Profile')

    def save(self, force_insert=False, force_update=False, using=None):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = 'catching_images/%s' % self.profile.user.username
        super(Catching, self).save()


class Senior(models.Model):
    name = models.CharField(max_length=15)
    #image = models.TextField(null=True)
    image = models.ImageField(upload_to='senior_image/', null=True)
    student_id = models.IntegerField(null=True)
    like_count = models.IntegerField(default=0)
    caught_count = models.IntegerField(default=0)
#    registered_time = models.DateTimeField(auto_now_add=True)
#    modified_time = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = 'senior_images/%s' % self.name
        super(Senior, self).save()


class Profile(models.Model):
    user = models.OneToOneField(User)
    is_freshmen = models.BooleanField(default=True)
    catching_count = models.IntegerField(default=0)
#    registered_time = models.DateTimeField(auto_now_add=True)
#    modified_time = models.DateTimeField(auto_now=True, blank=True, null=True)


class Chatting(models.Model):
    chat = models.TextField(null=False)
    profile = models.ForeignKey('Profile', null=True)
    catching = models.ForeignKey('Catching', null=True)
#    registered_time = models.DateTimeField(auto_now_add=True)
#    modified_time = models.DateTimeField(auto_now=True, blank=True, null=True)


class Like(models.Model):
    profile = models.ForeignKey('Profile')
    catching = models.ForeignKey('Catching')
#    registered_time = models.DateTimeField(auto_now_add=True)
#    modified_time = models.DateTimeField(auto_now=True, blank=True, null=True)


