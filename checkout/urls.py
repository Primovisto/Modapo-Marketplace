from django.conf.urls import url
from .views import pay_now
from home.views import search_items

urlpatterns = [
    url(r'^pay_now/(?P<id>\d+)', pay_now, name='pay_now_stripe'),
    url(r'^products/search/$', search_items, name='search'),
    


]
