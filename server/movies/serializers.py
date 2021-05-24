from rest_framework import serializers
from .models import Movie
from community.serializers import ReviewSerializer

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path',)


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)


    class Meta:
        model = Movie
        fields = ('id', 'movie_id', 'title', 'overview', 'release_date', 'poster_path', 'review_count', 'reviews')


