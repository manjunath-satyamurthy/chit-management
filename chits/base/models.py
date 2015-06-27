#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from django.db import models
from django.contrib.auth.models import AbstractUser

class ChitUser(AbstractUser):
    phone_number = models.CharField(max_length=16)

    class Meta(AbstractUser.Meta):
        abstract = False