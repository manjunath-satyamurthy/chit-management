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
            name='Member',
            fields=[
                ('mid', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=b'', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
