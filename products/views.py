# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


def product_page(request, id):
    product = get_object_or_404(Product, pk=id)
    product.views += 1
    product.save()
    return render(request, "products/productpage.html", {'product': product})
