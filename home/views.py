from django.shortcuts import render, get_object_or_404, render_to_response
from products.models import Product


# Create your views here.
def get_suggested(request):
    products = Product.objects.all().order_by('-id')[:8]
    return render(request, "index.html", {"products": products})


def product_page(request, id):
    product = get_object_or_404(Product, pk=id)
    product.views += 1
    product.save()
    return render(request, "products/productpage.html", {'product': product})


def search_items(request):
    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''

    products = Product.objects.filter(product__contains=search_text)

    return render_to_response('ajax_search.html', {'products': products})
