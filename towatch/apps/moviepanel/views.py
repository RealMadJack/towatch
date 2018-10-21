from collections.abc import Iterable
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MoviePanel, MovieGenre, Movie
from .serializers import MoviePanelSerializer, MovieGenreSerializer, MovieSerializer


class MoviePanelViewSet(viewsets.ReadOnlyModelViewSet):
    """Movie panel viewset"""
    queryset = MoviePanel.objects.prefetch_related('moviegenres', 'movies__moviegenre__moviepanel')
    serializer_class = MoviePanelSerializer
    lookup_field = 'slug'


class MovieGenreViewSet(viewsets.ReadOnlyModelViewSet):
    """Movie genre viewset"""
    queryset = MovieGenre.objects.select_related('moviepanel').prefetch_related(
        'movies__moviegenre__moviepanel', 'movies__moviepanel')
    serializer_class = MovieGenreSerializer
    lookup_field = 'slug'


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Movie viewset"""
    queryset = Movie.objects.select_related('moviepanel').prefetch_related('moviegenre', 'moviegenre__moviepanel')
    serializer_class = MovieSerializer


class MoviePanelView(APIView):
    """Movie panel api-view"""

    def get(self, request, *args, **kwargs):
        try:
            if kwargs:
                moviepanel = MoviePanel.objects.get(slug=kwargs['moviepanel_slug'])
            else:
                moviepanel = MoviePanel.objects.all()
            itr = True if isinstance(moviepanel, Iterable) else False
            serializer = MoviePanelSerializer(moviepanel, many=itr)
            return Response(serializer.data)
        except MoviePanel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MovieGenreView(APIView):
    """Movie genre api-view"""

    def get(self, request, *args, **kwargs):
        try:
            moviegenre = MovieGenre.objects.select_related().get(slug=kwargs['moviegenre_slug'])
            serializer = MovieGenreSerializer(moviegenre)
            return Response(serializer.data)
        except MovieGenre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MovieView(APIView):
    """Movie api-view"""

    def get(self, request, *args, **kwargs):
        try:
            movie = Movie.objects.get(slug=kwargs['movie_slug'])
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
