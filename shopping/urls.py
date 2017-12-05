from django.conf.urls import url
from shopping.views import add, remove, show, checkout


urlpatterns = [
    url(r'^add/$', add, name='shopping-cart-add'),
    url(r'^remove/$', remove, name='shopping-cart-remove'),
    url(r'^show/$', show, name='shopping-cart-show'),
    url(r'^checkout/$', checkout, name="checkout")

]

