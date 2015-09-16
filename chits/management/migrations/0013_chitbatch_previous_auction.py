# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20150810_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitbatch',
            name='previous_auction',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
