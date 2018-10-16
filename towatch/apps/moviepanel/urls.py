from django.urls import path
from rest_framework import routers

from .apps import MoviepanelConfig
from .views import MoviePanelViewSet, MovieGenreViewSet, MovieViewSet, MoviePanelView, MovieGenreView, MovieView

router = routers.DefaultRouter()
router.register(r'panels', MoviePanelViewSet)
router.register(r'genres', MovieGenreViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', view=MoviePanelView.as_view(), name='home'),
#     path('<slug:moviepanel_slug>/', view=MoviePanelView.as_view(), name='panel'),
#     path('<slug:moviepanel_slug>/genres/<slug:moviegenre_slug>/', view=MovieGenreView.as_view(), name='genre'),
#     path('<slug:moviepanel_slug>/<slug:movie_slug>/', view=MovieView.as_view(), name='movie'),
# ]
