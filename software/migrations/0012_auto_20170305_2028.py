# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0011_auto_20170305_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatting',
            name='senior',
        ),
        migrations.AddField(
            model_name='chatting',
            name='catching',
            field=models.ForeignKey(to='software.Catching', null=True),
        ),
    ]
