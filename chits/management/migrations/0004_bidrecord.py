# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20150703_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid_date', models.DateTimeField()),
                ('bid_amount', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('bidder', models.ForeignKey(related_name='bidders', to='management.Member')),
                ('chitbatch', models.ForeignKey(related_name='records', to='management.ChitBatch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
