from .models import Movie, Review, Comment
from .serializers import ReviewSerializer, CommentSerializer

from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# JWT 관련
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def review_create(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def review_delete_update(request, review_pk):

    if not request.user.user_reviews.filter(pk=review_pk).exists():
        return Response({ 'detail': '수정/삭제 권한이 없습니다.' }, status=status.HTTP_403_FORBIDDEN)

    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated]) 
def comment_create(request, review_pk):

    review = Review.objects.get(pk=review_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def comment_delete_update(request, review_pk, comment_pk):
    
    if not request.user.user_comments.filter(pk=comment_pk).exists():
        return Response({'detail': '수정/삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
