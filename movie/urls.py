from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'movie'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^movies/(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^s/', views.d),
    url(r'^test/', views.test),
    #url(r'^m', views.restframework.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)