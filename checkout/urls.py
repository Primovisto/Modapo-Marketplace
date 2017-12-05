from django.conf.urls import url
from .views import pay_now

urlpatterns = [
    url(r'^pay_now/(?P<id>\d+)', pay_now, name='pay_now_stripe'),
]
