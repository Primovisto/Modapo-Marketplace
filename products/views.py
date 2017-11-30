# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Product
from .forms import NewProductForm
from django.contrib.auth.decorators import login_required


def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


def product_page(request, id):
    product = get_object_or_404(Product, pk=id)
    product.views += 1
    product.save()
    return render(request, "products/productpage.html", {'product': product})


@login_required(login_url="/accounts/login?next=products/new/")
def add_new_product(request):
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect(product_page, product.pk)
    else:
        form = NewProductForm()
    return render(request, 'products/productform.html', {'form': form})


@login_required(login_url="accounts/login?next=products/edit/")
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()

            return redirect(product_page, product.pk)
    else:
        form = NewProductForm(instance=product)
    return render(request, 'products/productform.html', {'form': form})


