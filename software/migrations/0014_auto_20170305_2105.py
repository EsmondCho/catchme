# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0013_auto_20170305_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='registered_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 5, 12, 4, 42, 360095, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='registered_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 5, 12, 5, 0, 327024, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='senior',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='senior',
            name='registered_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 5, 12, 5, 10, 577860, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
