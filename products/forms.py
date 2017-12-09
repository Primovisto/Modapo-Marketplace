from django import forms
from .models import Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
                  'product',
                  'category',
                  'product_short_description',
                  'product_long_description',
                  'price',
                  'brand',
                  'brand_description',
                  'image')
