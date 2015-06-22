#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
'''
    File name: models.py
    Version: 0.1
    Author: Manjunath Satyamurthy
    Date created: 22/06/2015
    Date last modified: 22/06/2015
    Python Version: 2.7
'''
__author__ = "Manjunath Satyamurthy"
__status__ = "Development" # Other values are Production and Testing


from django.db import models
from django.contrib.auth.models import AbstractUser

class ChitUser(AbstractUser):
    phone_number = models.CharField(max_length=16)

    class Meta(AbstractUser.Meta):
        abstract = False