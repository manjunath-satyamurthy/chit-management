# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_chitbatch_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidrecord',
            name='bidder',
            field=models.ForeignKey(related_name='bids', to='management.Member'),
            preserve_default=True,
        ),
    ]
