# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20150809_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='bid_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
