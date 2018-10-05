from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MoviePanel
from .serializers import MoviePanelSerializer


class MoviePanelView(APIView):
    """Movie panel api-view"""

    def get(self, request, *args, **kwargs):
        try:
            if kwargs:
                moviepanel = MoviePanel.objects.get(slug=kwargs['moviepanel_slug'])
            else:
                moviepanel = MoviePanel.objects.first()
            serializer = MoviePanelSerializer(moviepanel)
            return Response(serializer.data)
        except MoviePanel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
