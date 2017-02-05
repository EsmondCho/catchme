from django.db import models


class Senior(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'senior_image/', default = 'senior_image/None/no-img.jpg')
    registered_time = models.DateTimeField(auto_now_add=True)

