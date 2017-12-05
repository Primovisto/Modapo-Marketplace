from django.http import HttpResponse
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from shopping.forms import CheckoutForm
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
import datetime
import stripe
from carton.cart import Cart
from products.models import Product


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.add(product, price=product.price)
    return HttpResponse("Added")


def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return HttpResponse("Removed")


def show(request):
    return render(request, 'shopping/show-cart.html')


def pay_now(request, id):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                products = get_object_or_404(Product, pk=id)
                customer = stripe.Charge.create(
                    amount=int(Product.price * 100),
                    currency='EUR',
                    description=Product.product,
                    card=form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError, e:
                messages.error(request, 'Your card was declined')

            if customer.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to take your payment")
        else:
            messages.error(request, "Unable to take your payment with that card")
    else:
        form = CheckoutForm()
        products = get_object_or_404(Product, pk=id)
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'products': products}
    args.update(csrf(request))
    return render(request, 'checkout.html', args)




