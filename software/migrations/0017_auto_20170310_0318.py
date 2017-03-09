# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0016_auto_20170309_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registered_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='catching',
            name='singo_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='singo',
            name='catching',
            field=models.ForeignKey(to='software.Catching'),
        ),
        migrations.AddField(
            model_name='singo',
            name='profile',
            field=models.ForeignKey(to='software.Profile'),
        ),
    ]
