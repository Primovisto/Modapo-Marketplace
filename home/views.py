from django.shortcuts import render, get_object_or_404, render_to_response
from products.models import Product


# Create your views here.
def index(request):
    """Home page"""
    latest_products = Product.objects.all().order_by('-id')[:4]
    all_products = Product.objects.all()
    return render(request, "index.html", {
        "latest_products": latest_products,
        "all_products": all_products
    })


def search_items(request):
    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''

    products = Product.objects.filter(product__contains=search_text)

    return render_to_response('ajax_search.html', {'products': products})
