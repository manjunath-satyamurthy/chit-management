# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20150829_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitbatch',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
