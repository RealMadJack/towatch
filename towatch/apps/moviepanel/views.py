from collections.abc import Iterable
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MoviePanel, MovieCategory
from .serializers import MoviePanelSerializer, MovieCategorySerializer


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


class MovieCategoryView(APIView):
    """Movie category api-view"""

    def get(self, request, *args, **kwargs):
        try:
            moviecategory = MovieCategory.objects.select_related().get(slug=kwargs['moviecategory_slug'])
            serializer = MovieCategorySerializer(moviecategory)
            return Response(serializer.data)
        except MovieCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
