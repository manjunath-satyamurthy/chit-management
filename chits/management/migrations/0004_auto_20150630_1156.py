# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20150630_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
