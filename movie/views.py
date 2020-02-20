# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Movie, Actor
import requests
#from .forms import
from .serializer import MovieSerializer

def d(request):
    #IMDB
    #url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt1375666"
    #headers = {
    #    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    #    'x-rapidapi-key': "132831c279msh58718fbc4258fa5p167406jsn1784599cce97"
    #}
    #response = requests.request("GET", url, headers=headers)
    #r = response.json()['cast']

    api_key = "b25b7ca4810bc48de0aadc57d2277175"

    response = requests.request("GET", "https://api.themoviedb.org/3/tv/4?api_key=" + api_key +
                                "&language=en-US")
    r = response.json()

    response = requests.request("GET", "https://api.themoviedb.org/3/tv/4/similar?api_key=" + api_key +
                                "&language=en-US&page=1")
    s = response.json()['results']

    # for movie in r:
    img = "https://image.tmdb.org/t/p/w500"
    # movie.vote_average = r['vote_average']
    # movie.original_language = r['original_language']
    # poster_path = r['poster_path']
    # img = img + poster_path

    return render(request, 'movie/s.html', {'r': r})

def title(request):

    api_key = "b25b7ca4810bc48de0aadc57d2277175"
    query = "fight club"
    response = requests.request("GET", "https://api.themoviedb.org/3/search/movie?api_key="+api_key+
                                "&language=en-US&query="+query+"&page=1&include_adult=false")

    # How I retrive JSon data
    img = "https://image.tmdb.org/t/p/w500"
    r = response.json()['results'][0]
    overview = r['overview']
    vote_count = r['vote_count']
    vote_average = r['vote_average']
    release_date = r['release_date']
    original_language = r['original_language']
    poster_path = r['poster_path']
    img = img + poster_path

    return render(request,'movie/s.html',{'r':r})

class restframework(APIView):
    # queryset = Movie.objects.all()
    # serializer_class = MovieSerializer
    def get(self, request):
        m = Movie.objects.all()
        #s = "https://api.themoviedb.org/3/search/movie?api_key=b25b7ca4810bc48de0aadc57d2277175&language=en-US&query=fightclub&page=1&include_adult=false"
        serializer = MovieSerializer(m, many=True)
        return Response(serializer.data)

    def put(self, request):
        m = Movie.object.get(pk=1)
        serializer = MovieSerializer(m, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'upd succ'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    api_key = "b25b7ca4810bc48de0aadc57d2277175"
    response = requests.request("GET", "https://api.themoviedb.org/3/trending/all/day?api_key="+api_key)
    r = response.json()['results']

    context = {
        'trending' : r,
    }
    return render(request,'movie/index.html',context)

def movies(request):
    api_key = "b25b7ca4810bc48de0aadc57d2277175"
    response = requests.request("GET", "https://api.themoviedb.org/3/movie/top_rated?api_key=" + api_key +
                                "&language=en-US&page=1")
    r = response.json()['results']

    response = requests.request("GET", "https://api.themoviedb.org/3/movie/popular?api_key="+api_key+
                                "&language=en-US&page=1")
    p = response.json()['results']

    response = requests.request("GET", "https://api.themoviedb.org/3/movie/now_playing?api_key="+api_key+
                                "&language=en-US")
    n = response.json()['results']

    response = requests.request("GET", "https://api.themoviedb.org/3/movie/upcoming?api_key=" + api_key +
                                "&language=en-US")
    u = response.json()['results']


    context = {
        'rmovies' : r,
        'pmovies' : p,
        'nmovies' : n,
        'umovies' : u,
    }
    return render(request,'movie/movies.html',context)

def detail(request, movie_id):
    #movie = get_object_or_404(Movie,pk=movie_id)
    #movie = Movie.objects.get(pk=movie_id)
    #actors = get_object_or_404(Actor, Movie=movie)
    #try :
    #   actors = Actor.objects.filter(Movie=movie)
    #except Actor.DoesNotExist:
    #    actors = None

    # How I retrive JSon data
    #img = "https://image.tmdb.org/t/p/w500"
    #movie.overview = r['overview']
    #movie.vote_count = r['vote_count']
    #movie.vote_average = r['vote_average']
    #movie.release_date = r['release_date']
    #movie.original_language = r['original_language']
    #poster_path = r['poster_path']
    #movie.img = img + poster_path
    #def movie_info2(request):
    #    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt1375666"
    #    headers = {
    #        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    #        'x-rapidapi-key': "132831c279msh58718fbc4258fa5p167406jsn1784599cce97"
    #    }
    #    response = requests.request("GET", url, headers=headers)
    #movi_info(request)

    api_key = "b25b7ca4810bc48de0aadc57d2277175"

    response = requests.request("GET", "https://api.themoviedb.org/3/movie/" + movie_id + "?api_key=" + api_key +
                                "&language=en-US&page=1")
    r = response.json()

    response = requests.request("GET", "https://api.themoviedb.org/3/movie/" + movie_id +"/similar?api_key=" + api_key +
                                "&language=en-US&page=1")
    s = response.json()['results']

    #response = requests.request("GET","https://api.themoviedb.org/3/movie/" + movie_id + "/images?api_key=" + api_key +
    #                            "&language=en-US")
    #images = response.json()['results']

    response = requests.request("GET","https://api.themoviedb.org/3/movie/" + movie_id + "/reviews?api_key=" + api_key +
                                "&language=en-US&page=1")
    reviews = response.json()['results']

    response = requests.request("GET",
                                "https://api.themoviedb.org/3/movie/" + movie_id + "/credits?api_key=" + api_key +
                                "&language=en-US&page=1")
    casts = response.json()['cast']
    casts = casts[:6]

    context = {
        'movie': r,
        'smovie' : s,
        'reviews' : reviews,
        'casts' : casts
    }
    return render(request,'movie/detail.html',context)


def test(request):

    return render(request, 'movie/test.html')