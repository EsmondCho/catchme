# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0009_auto_20170304_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='catching',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
