# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0021_chitbatch_is_multiple_auctions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidrecord',
            name='is_multiple_auctions',
        ),
        migrations.AddField(
            model_name='bidrecord',
            name='bid_count',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
