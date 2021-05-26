from rest_framework import serializers
from .models import Comment, Review
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'created_at', 'updated_at', 'content', )
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'created_at', 'updated_at', 'title', 'content', 'rate', 'comments', 'comment_count', )
        read_only_fields = ('movie',)