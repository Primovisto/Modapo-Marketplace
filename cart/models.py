from django.db import models
from products.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product)
