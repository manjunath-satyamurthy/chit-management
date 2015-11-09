# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20150729_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitbatch',
            name='next_auction',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
