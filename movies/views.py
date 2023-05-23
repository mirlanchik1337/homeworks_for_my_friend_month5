from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers import *
from movies.models import *
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def director_list(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
def get_director(request, id):
    director = get_object_or_404(Director, id=id)
    serializer = DirectorSerializer(director, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
def get_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        movies = Review.objects.all()
        serializer = ReviewSerializer(movies, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
def get_review(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(review ,many=False)
    return Response(data=serializer.data)
