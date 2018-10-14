from rest_framework import serializers
from .models import MoviePanel, MovieGenre, Movie


class MoviePanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePanel
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
