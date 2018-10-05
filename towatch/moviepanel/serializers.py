from rest_framework import serializers
from .models import MoviePanel


class MoviePanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePanel
        fields = ('name', 'created', 'modified')
