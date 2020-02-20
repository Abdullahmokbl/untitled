from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.logina, name='login'),
    url(r'^logout/', views.logouta, name='logout'),
    url(r'^sign/', views.sign, name='sign'),
    url(r'^social-auth/', include('social_django.urls', namespace="social")),
]