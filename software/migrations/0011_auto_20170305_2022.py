# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0010_catching_modified_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatting',
            old_name='user',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='profile',
        ),
    ]
