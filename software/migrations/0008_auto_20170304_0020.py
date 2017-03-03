# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0007_auto_20170303_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catching',
            name='senior',
            field=models.ForeignKey(to='software.Senior', null=True),
        ),
    ]
