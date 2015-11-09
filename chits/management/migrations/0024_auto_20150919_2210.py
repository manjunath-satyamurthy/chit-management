# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0023_auto_20150919_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidrecord',
            name='shortage',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chitbatch',
            name='shortage',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paymentrecord',
            name='paid',
            field=models.IntegerField(default=1, null=True, blank=True, choices=[(-1, b'UNKNOWN'), (1, b'PAID'), (0, b'UN_PAID'), (2, b'CHIT_BENIFIT')]),
            preserve_default=True,
        ),
    ]
