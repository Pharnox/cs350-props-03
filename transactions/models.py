# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from properties.models import Property

TRANS_TYPES = (('offer', 'OFFER'), ('cancel', 'CANCEL OFFER'), ('close', 'CLOSE'))

class Transaction(models.Model):
    prop = models.ForeignKey(Property, related_name='transactions')
    trans_date = models.DateTimeField(auto_now=True)
    trans_type = models.CharField(max_length=64, choices=TRANS_TYPES)

