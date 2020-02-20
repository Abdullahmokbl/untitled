from django.conf.urls import url
from . import views

app_name = 'tv'

urlpatterns = [
    url(r'^tv/', views.tv, name='tv'),
    url(r'^series/(?P<tv_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search', views.search.as_view(), name='search')
]
