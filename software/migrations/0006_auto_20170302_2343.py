# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0005_auto_20170302_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catching',
            old_name='is_succeed',
            new_name='is_in_pocket',
        ),
        migrations.AddField(
            model_name='catching',
            name='confidence',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='senior',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
