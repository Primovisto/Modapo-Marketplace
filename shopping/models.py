from __future__ import unicode_literals

from django.db import models
from products.models import Product
from accounts.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)

    def __unicode__(self):

        return self.product
