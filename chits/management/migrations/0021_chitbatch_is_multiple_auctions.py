# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_bidrecord_is_multiple_auctions'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitbatch',
            name='is_multiple_auctions',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
