# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_auto_20150917_1556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bidrecord',
            options={'get_latest_by': 'bid_date'},
        ),
    ]
