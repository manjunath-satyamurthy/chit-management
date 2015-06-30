# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20150627_0743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='uid',
            new_name='user',
        ),
    ]
