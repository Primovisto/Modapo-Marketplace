from django.conf.urls import url
import views
from home.views import search_items

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/top', views.top_posts),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name='edit'),
    url(r'^products/search/$', search_items, name='search'),
]
