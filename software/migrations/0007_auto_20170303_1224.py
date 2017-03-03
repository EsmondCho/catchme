# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0006_auto_20170302_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catching',
            name='image',
            field=models.ImageField(null=True, upload_to=b'catching_image/'),
        ),
        migrations.AlterField(
            model_name='senior',
            name='image',
            field=models.ImageField(null=True, upload_to=b'senior_image/'),
        ),
    ]
