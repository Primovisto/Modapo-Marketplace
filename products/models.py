
from __future__ import unicode_literals
from django.utils import timezone
import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

User = settings.AUTH_USER_MODEL


# Create your models here.
class Product(models.Model):

    seller = models.ForeignKey('accounts.User')
    product = models.CharField(max_length=35, default='')
    category = models.ForeignKey('Category', null=True, blank=True)
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


    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "EUR",
            "item_name": self.product,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.product


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name

