# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20150703_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid', models.IntegerField(null=True, blank=True)),
                ('bid_date', models.DateTimeField()),
                ('chitbatch', models.ForeignKey(related_name='payments', to='management.ChitBatch')),
                ('member', models.ForeignKey(related_name='payments', to='management.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bidrecord',
            name='payment_record',
            field=models.ManyToManyField(to='management.PaymentRecord'),
            preserve_default=True,
        ),
    ]
