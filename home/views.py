from django.shortcuts import render
from products.models import Product


# Create your views here.
def get_suggested(request):
    products = Product.objects.all().order_by('-id')[:10]
    return render(request, "index.html", {"products": products})
