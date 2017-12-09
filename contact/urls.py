from django.conf.urls import url
from .views import contact, thanks
from home.views import search_items


urlpatterns = [
    url(r'^$', contact, name='contact'),
    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^products/search/$', search_items, name='search'),
    url(r'^products/(?P<id>\d+)/', search_items, name='search'),

]
