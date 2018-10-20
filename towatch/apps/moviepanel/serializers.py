from rest_framework import serializers
from .models import MoviePanel, MovieGenre, Movie


class MoviePanelCleanSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='moviepanel:moviepanel-detail', lookup_field='slug')

    class Meta:
        model = MoviePanel
        fields = '__all__'


class MovieGenreCleanSerializer(serializers.ModelSerializer):
    moviepanel = MoviePanelCleanSerializer()
    url = serializers.HyperlinkedIdentityField(view_name='moviepanel:moviegenre-detail', lookup_field='slug')

    class Meta:
        model = MovieGenre
        fields = '__all__'


class MovieCleanSerializer(serializers.ModelSerializer):
    moviegenre = MovieGenreCleanSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='moviepanel:movie-detail')

    class Meta:
        model = Movie
        fields = '__all__'


class MoviePanelSerializer(serializers.ModelSerializer):
    moviegenres = MovieGenreCleanSerializer(many=True)
    movies = MovieCleanSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='moviepanel:moviepanel-detail', lookup_field='slug')

    class Meta:
        model = MoviePanel
        fields = '__all__'
        lookup_field = 'slug'


class MovieGenreSerializer(serializers.ModelSerializer):
    moviepanel = MoviePanelCleanSerializer()
    movies = MovieCleanSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='moviepanel:moviegenre-detail', lookup_field='slug')

    class Meta:
        model = MovieGenre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    moviepanel = MoviePanelCleanSerializer()
    moviegenre = MovieGenreCleanSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='moviepanel:movie-detail')

    class Meta:
        model = Movie
        fields = '__all__'
