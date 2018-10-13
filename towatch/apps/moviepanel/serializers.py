from rest_framework import serializers
from .models import MoviePanel, MovieCategory


class MoviePanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePanel
        fields = '__all__'


class MovieCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategory
        fields = '__all__'
