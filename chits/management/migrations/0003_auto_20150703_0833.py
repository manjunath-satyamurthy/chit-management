# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_chitbatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitbatch',
            name='state',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
