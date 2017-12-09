
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Product(models.Model):

    CATEGORY_CHOICES = (
        ('Shoes', 'Shoes'),
        ('Hats', 'Hats'),
        ('Accessories', 'Accessories'),
        ('Coats', 'Coats'),
        ('Trousers', 'Trousers'),
        ('Suits', 'Suits'),
        ('Dresses', 'Dresses'),
        ('Shirts', 'Shirts'),
        ('t-shirts', 't-shirts')

    )

    seller = models.ForeignKey('accounts.User')
    product = models.CharField(max_length=35, default='')
    category = models.CharField(max_length=35, default='', choices=CATEGORY_CHOICES)
    product_short_description = models.TextField(default='')
    product_long_description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=35, default='')
    brand_description = models.TextField(default='')
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.product

