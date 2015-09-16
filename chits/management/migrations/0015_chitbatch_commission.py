# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_remove_chitbatch_previous_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitbatch',
            name='commission',
            field=models.SmallIntegerField(default=3),
            preserve_default=True,
        ),
    ]
