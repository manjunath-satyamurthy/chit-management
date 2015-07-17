# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20150703_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitbatch',
            name='start_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
