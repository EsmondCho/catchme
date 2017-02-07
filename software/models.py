from django.db import models


class Senior(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'senior_image/', null=True)
    registered_time = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = 'senior_pictures/%s' % self.name
        super(Senior, self).save()

