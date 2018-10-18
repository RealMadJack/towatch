from django.urls import path
from rest_framework import routers

from .apps import MoviepanelConfig
from .views import MoviePanelViewSet, MovieGenreViewSet, MovieViewSet

app_name = MoviepanelConfig.verbose_name

router = routers.DefaultRouter()
router.register(r'panels', MoviePanelViewSet)
router.register(r'genres', MovieGenreViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    # path('panels/', MoviePanelList.as_view(), name='panel-list'),
    # path('panels/<slug:moviepanel_slug>/', view=MoviePanelView.as_view(), name='panel'),
    # path('genres/', view=MovieGenreList.as_view(), name='genre-list'),
    # path('genres/<slug:moviegenre_slug>/', view=MovieGenreView.as_view(), name='genre'),
    # path('', view=MoviePanelView.as_view(), name='home'),
    # path('<slug:moviepanel_slug>/<slug:movie_slug>/', view=MovieView.as_view(), name='movie'),
] + router.urls
