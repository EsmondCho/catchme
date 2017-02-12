# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0002_auto_20170206_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senior',
            name='image',
        ),
    ]
