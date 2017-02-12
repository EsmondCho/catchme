# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_remove_senior_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='senior',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
