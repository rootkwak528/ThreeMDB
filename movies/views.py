from operator import imod
from .models import Movie
from .serializers import MovieSerializer
from community.models import Review, Comment
from community.serializers import ReviewSerializer

from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from decouple import config


TMDB_API_KEY = config('TMDB_API_KEY')


@api_view(['POST'])
def movie_create(request):
    print('hello')

    movie_id = request.data.get('id')
    movie = Movie.objects.filter(movie_id=movie_id)
    print('hello1')

    if not movie.exists():
        print('hello2')
        movie_data = {
            'movie_id': movie_id,
            'title': request.data.get('title'),
            'overview': request.data.get('overview'),
            'release_date': request.data.get('release_date'),
            'poster_path': request.data.get('poster_path'),
        }
        

        print('hello3')
        serializer = MovieSerializer(data=movie_data)
        if serializer.is_valid(raise_exception=True):

            print('hello4')
            serializer.save()

            print('hello5')
            return Response(serializer.data)

    else:
        print('hello6')
        try:
            reviews = Review.objects.select_related('user')
            comments = Comment.objects.select_related('user')
            print('hello7')

            movie = Movie.objects.prefetch_related(
                Prefetch('reviews', queryset=reviews),
                Prefetch('reviews__comments', queryset=comments)
                ).get(pk=movie[0].pk)

            print('hello8')

        except:
            print('hello9')
            return Response(status=status.HTTP_404_NOT_FOUND)

        print('hello10')
        serializer = MovieSerializer(movie)
        print('hello11')
        return Response(serializer.data, status=status.HTTP_200_OK)
