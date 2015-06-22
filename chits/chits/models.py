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


from django.db.models import CharField, SmallIntegerField, Model, \
    DateTimeField


class User(Model):
    """
    The Only user of the application
    """
    username = CharField(max_length=25, unique=True)
    first_name = CharField(max_length=25)
    last_name = CharField(max_length=25)
    phone_number = IntegerField(maxlength=15)
    email = EmailField(maxlenth=25, unique=True)
    created_on = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s - %s" % (self.username, self.get_source_display())

    def __repr__(self):
        return "<User: %s>" % self.__str__()