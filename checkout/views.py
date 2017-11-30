# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from checkout.forms import CheckoutForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from products.models import Product
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="accounts/login?next=checkout/buy_now")
def buy_now(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                product = get_object_or_404(Product, pk=id)
                customer = stripe.Charge.create(
                    amount=999,
                    currency="EUR",
                    description=product.product,
                    card=form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('product'))
            else:
                messages.error(request, "unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    else:
        form = CheckoutForm()
        product = get_object_or_404(Product, pk=id)

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'product': product}
    args.update(csrf(request))

    return render(request, 'checkout.html', args)
