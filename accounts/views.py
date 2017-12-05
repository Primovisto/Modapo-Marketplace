from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.conf import settings
from products.models import Product
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered and are now logged into your account")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "Unable to log you in at this time.")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


@login_required(login_url='/login?next=profile')
def profile(request):
    products = Product.objects.all().order_by('-created_date')
    return render(request, "profile.html", {'products': products})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
