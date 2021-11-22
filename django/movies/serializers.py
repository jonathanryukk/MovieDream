from rest_framework import serializers
from .models import Genre, Movie, UserRank

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRank
        fields = '__all__'
        read_only_fields = ('user', 'movie')