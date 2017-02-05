# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(default=b'senior_image/None/no-img.jpg', upload_to=b'senior_image/')),
                ('registered_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
