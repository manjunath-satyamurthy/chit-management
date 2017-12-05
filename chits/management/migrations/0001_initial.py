# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BidRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid_date', models.DateField()),
                ('bid_amount', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('bid_count', models.SmallIntegerField(default=1)),
                ('shortage', models.IntegerField(default=0)),
            ],
            options={
                'get_latest_by': 'bid_date',
            },
        ),
        migrations.CreateModel(
            name='ChitBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
                ('no_of_members', models.SmallIntegerField(default=0)),
                ('principal', models.IntegerField()),
                ('commission_percent', models.IntegerField(default=3)),
                ('balance', models.IntegerField(default=0)),
                ('shortage', models.IntegerField(default=0)),
                ('emi', models.IntegerField()),
                ('period', models.SmallIntegerField()),
                ('dues', models.SmallIntegerField()),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('next_auction', models.DateField(null=True)),
                ('is_multiple_auction', models.BooleanField(default=False)),
                ('state', models.BooleanField(default=True)),
                ('end_date', models.TimeField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mid', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
                ('phone_number', models.CharField(unique=True, max_length=20)),
                ('photo', models.ImageField(upload_to=b'', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid', models.IntegerField(default=1, null=True, blank=True, choices=[(-1, b'UNKNOWN'), (1, b'PAID'), (0, b'UN_PAID'), (2, b'CHIT_BENIFIT')])),
                ('bid_date', models.DateField()),
                ('chitbatch', models.ForeignKey(related_name='payments', to='management.ChitBatch')),
                ('member', models.ForeignKey(related_name='payments', to='management.Member')),
            ],
        ),
        migrations.AddField(
            model_name='chitbatch',
            name='members',
            field=models.ManyToManyField(to='management.Member'),
        ),
        migrations.AddField(
            model_name='chitbatch',
            name='user',
            field=models.ForeignKey(related_name='chit_batches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bidrecord',
            name='bidder',
            field=models.ForeignKey(related_name='bids', to='management.Member'),
        ),
        migrations.AddField(
            model_name='bidrecord',
            name='chitbatch',
            field=models.ForeignKey(related_name='records', to='management.ChitBatch'),
        ),
        migrations.AddField(
            model_name='bidrecord',
            name='payment_record',
            field=models.ManyToManyField(to='management.PaymentRecord'),
        ),
    ]
