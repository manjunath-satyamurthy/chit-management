# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_auto_20150917_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidrecord',
            name='is_multiple_auctions',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
