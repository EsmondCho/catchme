# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior',
            name='image',
            field=models.ImageField(null=True, upload_to=b'senior_image/'),
        ),
    ]
