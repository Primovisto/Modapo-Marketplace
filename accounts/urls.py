from django.conf.urls import url
from .views import logout, profile, login, register, edit_profile, change_password
from home.views import search_items


urlpatterns = [
    url(r'^register', register, name='register'),
    url(r'^profile', profile, name='profile'),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^change_password/$', change_password, name='change_password'),
    url(r'^login', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^products/search/$', search_items, name='search'),
]
