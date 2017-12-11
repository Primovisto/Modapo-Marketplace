from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from .models import Product, Category
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


@login_required(login_url="/accounts/login?next=products/edit/")
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


@login_required(login_url="/accounts/login?next=products/delete/")
def delete_product(request, id):
    product = Product.objects.filter(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('products'))


def category_list(request):
    categories = Category.objects.all()

    return render(request, 'products/category_list.html', {'categories': categories})





