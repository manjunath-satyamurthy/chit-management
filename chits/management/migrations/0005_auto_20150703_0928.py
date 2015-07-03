# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_bidrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitbatch',
            name='end_date',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
