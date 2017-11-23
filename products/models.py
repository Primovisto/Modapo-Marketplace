# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Product(models.Model):

    seller = models.ForeignKey('accounts.User')
    product = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.product
