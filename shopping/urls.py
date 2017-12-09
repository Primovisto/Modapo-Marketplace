from django.conf.urls import url
from shopping.views import add, remove, show, checkout, user_cart
from home.views import search_items

urlpatterns = [
    url(r'^add/$', add, name='shopping-cart-add'),
    url(r'^remove/$', remove, name='shopping-cart-remove'),
    url(r'^show/$', show, name='shopping-cart-show'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^$', user_cart, name='cart'),
    url(r'^products/search/$', search_items, name='search'),
    url(r'^show/products/search/$', search_items, name='search'),
    url(r'^add/products/search/$', search_items, name='search'),
    url(r'^remove/products/search/$', search_items, name='search'),
    url(r'^checkout/products/search/$', search_items, name='search'),
]
