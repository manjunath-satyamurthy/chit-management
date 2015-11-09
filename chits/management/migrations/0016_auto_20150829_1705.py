# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_chitbatch_commission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chitbatch',
            name='commission',
        ),
        migrations.AddField(
            model_name='chitbatch',
            name='commission_percent',
            field=models.IntegerField(default=3),
            preserve_default=True,
        ),
    ]
