# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0014_auto_20170305_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='catching',
            name='chatting_count',
            field=models.IntegerField(default=0),
        ),
    ]
