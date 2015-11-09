# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_chitbatch_next_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidrecord',
            name='bid_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
