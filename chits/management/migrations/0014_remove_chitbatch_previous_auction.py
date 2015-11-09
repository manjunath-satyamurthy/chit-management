# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_chitbatch_previous_auction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chitbatch',
            name='previous_auction',
        ),
    ]
