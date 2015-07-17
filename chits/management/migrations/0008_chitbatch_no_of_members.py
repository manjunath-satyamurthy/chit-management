# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20150705_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitbatch',
            name='no_of_members',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
