from django.shortcuts import render, get_object_or_404
from .models import Movie
from .serializers import ReviewSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# JWT 관련
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def review_create(request, movie_pk):
    print('server recieve')
    if request.method == 'GET':
        serializer = ReviewSerializer(request.user.todos, many=True)
        return Response(serializer.data)
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)