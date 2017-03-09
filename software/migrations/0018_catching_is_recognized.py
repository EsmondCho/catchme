# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0017_auto_20170310_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='catching',
            name='is_recognized',
            field=models.BooleanField(default=True),
        ),
    ]
