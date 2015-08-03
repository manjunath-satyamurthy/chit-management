# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_chitbatch_no_of_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='paid',
            field=models.IntegerField(default=1, null=True, blank=True, choices=[(-1, b'UNKNOWN'), (1, b'PAID'), (0, b'UN_PAID')]),
            preserve_default=True,
        ),
    ]
