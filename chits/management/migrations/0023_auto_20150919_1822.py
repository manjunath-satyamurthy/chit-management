# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_auto_20150919_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chitbatch',
            old_name='is_multiple_auctions',
            new_name='is_multiple_auction',
        ),
    ]
