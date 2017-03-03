# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0008_auto_20170304_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catching',
            old_name='user',
            new_name='profile',
        ),
    ]
