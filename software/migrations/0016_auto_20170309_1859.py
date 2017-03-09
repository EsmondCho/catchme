# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0015_catching_chatting_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_freshmen',
            new_name='is_freshman',
        ),
    ]
