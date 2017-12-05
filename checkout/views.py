from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from shopping.forms import CheckoutForm
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
from products.models import Product
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="/accounts/login?next=checkout/pay_now")
def pay_now(request, id):
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
