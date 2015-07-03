# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChitBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
                ('principal', models.IntegerField()),
                ('emi', models.IntegerField()),
                ('period', models.SmallIntegerField()),
                ('dues', models.SmallIntegerField()),
                ('start_date', models.DateTimeField()),
                ('start_time', models.TimeField()),
                ('state', models.BooleanField()),
                ('end_date', models.TimeField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(to='management.Member')),
                ('user', models.ForeignKey(related_name='chit_batches', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
