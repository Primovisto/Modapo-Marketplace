from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class CartProduct(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return "{0} ({1})".format(self.product.product, self.quantity)
