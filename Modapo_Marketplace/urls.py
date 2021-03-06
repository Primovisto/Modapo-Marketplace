"""Modapo_Marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.conf import settings
from products import urls as products_urls
from checkout import urls as checkout_urls
from accounts import urls as accounts_urls
from home.views import index, search_items
from contact import urls as contact_urls
from shopping import urls as shopping_urls
from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views


urlpatterns = [

    url(r'^accounts/', include(accounts_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include(products_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', index, name='index'),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^shopping-cart/', include(shopping_urls)),
    url(r'^products/search/$', search_items, name='search'),
url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),


]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
