
from django.conf.urls import url
from .views import all_products, product_page, add_new_product, edit_product

urlpatterns = [

    url(r'^$', all_products, name='products'),
    url(r'^(?P<id>\d+)/$', product_page, name='productpage'),
    url(r'^new/$', add_new_product, name='new'),
    url(r'^(?P<id>\d+)/edit$', edit_product, name='edit'),

]
