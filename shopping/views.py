from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from shopping.forms import CheckoutForm
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from shopping.models import CartItem
from carton.cart import Cart
from products.models import Product


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.add(product, price=product.price)
    return render(request, 'shopping/show-cart.html')


def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return render(request, 'shopping/show-cart.html')


def show(request):
    return render(request, 'shopping/show-cart.html')


@login_required(login_url="/accounts/login?next=shopping-cart/checkout")
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                product = get_object_or_404(Product, pk=id)
                customer = stripe.Charge.create(
                    amount=int(Product.price * 100),
                    currency='EUR',
                    description=Product.product,
                    card=form.cleaned_data['stripe_id'],
                )

                if customer.paid:
                    messages.success(request, "You have successfully paid")
                    return redirect(reverse('index'))

                else:
                    messages.error(request, "Unable to take your payment")

            except stripe.error.CardError, e:
                messages.error(request, 'Your card was declined')
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        form = CheckoutForm()

    product = get_object_or_404(Product, pk=id)
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'product': product}
    args.update(csrf(request))

    return render(request, 'checkout.html', args)


@login_required(login_url="/accounts/login")
def user_cart(request):
    cartItems = CartItem.objects.filter(user=request.id)
    total = 0
    for item in cartItems:
        total += item.product.price

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=form.cleaned_data['stripe_id'],
                )

                if customer.paid:
                    messages.success(request, "You have successfully paid")
                    Product.objects.filter(user=request.user).delete()
                    return redirect(reverse('products'))

                else:
                    messages.error(request, "Unable to take payment")

            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined. Please try again")

        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        if len(cartItems) == 0:
            return render(request, 'shopping/empty-cart.html')

        form = CheckoutForm()

    args = {'form': form,
            'items': cartItems,
            'total': total,
            'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'shopping/show-cart.html', args)
