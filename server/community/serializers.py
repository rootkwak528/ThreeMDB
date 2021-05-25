from rest_framework import serializers
from .models import Comment, Review


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content',)
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rate', 'comments', 'comment_count',)
        read_only_fields = ('movie',)