from .serializers import MovieSerializer
from django.shortcuts import render, get_object_or_404
from .models import Movie

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def movie_create(request):
    db_movie = Movie.objects.filter(movie_id=request.data.get('id'))

    if not len(db_movie):
        movie = {
            'movie_id': request.data.get('id'),
            'title': request.data.get('title'),
            'overview': request.data.get('overview'),
            'release_date': request.data.get('release_date'),
            'poster_path': request.data.get('poster_path'),
        }
        
        serializer = MovieSerializer(data=movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    else:
        try:
            movie = Movie.objects.prefetch_related('reviews').filter(pk=db_movie[0].pk)[0]
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
