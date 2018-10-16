from rest_framework import serializers
from .models import MoviePanel, MovieGenre, Movie


class MovieSerializer(serializers.ModelSerializer):
    moviepanel = serializers.StringRelatedField()
    moviegenre = serializers.StringRelatedField(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='movie-detail')

    class Meta:
        model = Movie
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='moviegenre-detail')

    class Meta:
        model = MovieGenre
        fields = '__all__'


class MoviePanelSerializer(serializers.ModelSerializer):
    moviegenres = serializers.StringRelatedField(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='moviepanel-detail')

    class Meta:
        model = MoviePanel
        fields = '__all__'
