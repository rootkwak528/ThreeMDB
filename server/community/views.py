from django.shortcuts import render, get_object_or_404
from .models import Movie, Review
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
        serializer = ReviewSerializer(request.user.user_reviews.filter(movie_id=movie_pk), many=True)
        return Response(serializer.data)
    else:
        try:
            movie = Movie.objects.prefetch_related('reviews').filter(pk=movie_pk)[0]
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if not request.user.user_reviews.filter(pk=review_pk).exists():
        return Response({'detail': '수정/삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    review.delete()
    return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)