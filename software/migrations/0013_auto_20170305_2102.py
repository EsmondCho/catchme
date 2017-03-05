# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0012_auto_20170305_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatting',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='chatting',
            name='registered_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 5, 12, 2, 34, 261357, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
