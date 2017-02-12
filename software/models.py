from django.db import models


class Senior(models.Model):
    name = models.CharField(max_length=20)
    image = models.TextField(null=True)
    registered_time = models.DateTimeField(auto_now_add=True)

