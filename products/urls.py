
from django.conf.urls import url
from .views import all_products, product_page, add_new_product, edit_product, delete_product
from home.views import search_items

urlpatterns = [

    url(r'^$', all_products, name='products'),
    url(r'^(?P<id>\d+)/$', product_page, name='productpage'),
    url(r'^new/$', add_new_product, name='new'),
    url(r'^(?P<id>\d+)/edit/$', edit_product, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', delete_product, name='delete_product'),
    url(r'^products/search/$', search_items, name='search'),
    url(r'^new/products/search/$', search_items, name='search'),
    url(r'^delete/(?P<id>\d+)/products/search$', search_items, name='search'),



]
