from django.shortcuts import render
from products.models import Product


# Create your views here.
def get_index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})
