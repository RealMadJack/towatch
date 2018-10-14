from django.urls import path

from .apps import MoviepanelConfig
from .views import MoviePanelView, MovieGenreView, MovieView

app_name = MoviepanelConfig.verbose_name

# trail  slash
urlpatterns = [
    path('', view=MoviePanelView.as_view(), name='home'),
    path('<slug:moviepanel_slug>/', view=MoviePanelView.as_view(), name='panel'),
    path('<slug:moviepanel_slug>/genres/<slug:moviegenre_slug>/', view=MovieGenreView.as_view(), name='genre'),
    path('<slug:moviepanel_slug>/<slug:movie_slug>/', view=MovieView.as_view(), name='movie'),
]
