# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from movie.models import Movie, Actor
import requests
#from .forms import
#from .serializer import MovieSerializer
from django.views.generic import TemplateView, ListView

class search(ListView):
    model = Movie
    template_name = 'movie/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            #return Movie.objects.filter(title__icontains=query)
            api_key = "b25b7ca4810bc48de0aadc57d2277175"
            response = requests.request("GET","https://api.themoviedb.org/3/search/movie?api_key="+api_key+
                                              "&language=en-US&query="+query+"&page=1&include_adult=false")
            return response.json()['results']


def tv(request):
    try:
        api_key = "b25b7ca4810bc48de0aadc57d2277175"
        response = requests.request("GET", "https://api.themoviedb.org/3/tv/top_rated?api_key=" + api_key +
                                    "&language=en-US")
        r = response.json()['results']

        response = requests.request("GET", "https://api.themoviedb.org/3/tv/popular?api_key="+api_key+
                                    "&language=en-US&page=1")
        p = response.json()['results']

        response = requests.request("GET", "https://api.themoviedb.org/3/tv/on_the_air?api_key="+api_key+
                                    "&language=en-US")
        n = response.json()['results']

        response = requests.request("GET", "https://api.themoviedb.org/3/tv/latestapi_key=" + api_key +
                                    "&language=en-US")
        #l = response.json()['results']
    except requests.ConnectionError:
        return render(request, 'tv/tv.html')

    context = {
        'rseries' : r,
        'pseries' : p,
        'nseries' : n,

    }
    return render(request,'tv/tv.html',context)

def detail(request, tv_id):
    try:
        api_key = "b25b7ca4810bc48de0aadc57d2277175"

        response = requests.request("GET", "https://api.themoviedb.org/3/tv/" + tv_id + "?api_key=" + api_key +
                                    "&language=en-US")
        r = response.json()

        response = requests.request("GET", "https://api.themoviedb.org/3/tv/" + tv_id + "/similar?api_key=" + api_key +
                                    "&language=en-US&page=1")
        s = response.json()['results']
    except requests.ConnectionError:
        return render(request, 'tv/test.html')


    context = {
        'movie': r,
        'sseries': s,
    }
    return render(request, 'tv/detail.html', context)

