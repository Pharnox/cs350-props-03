# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Message(models.Model):
    """ Implement a model for the messenger app called __Message__ (messenger/
    models.py). This model has the following attributes: a subject line, the 
    message text, date created, and email of the person submitting the message.
    """
    subject = models.CharField(max_length=255)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    sender_email = models.EmailField()
    