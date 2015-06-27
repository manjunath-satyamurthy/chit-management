# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(default=datetime.datetime(2015, 6, 27, 7, 43, 39, 452816, tzinfo=utc), unique=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
