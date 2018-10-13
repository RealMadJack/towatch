from django.urls import path

from .apps import MoviepanelConfig
from .views import MoviePanelView, MovieCategoryView

app_name = MoviepanelConfig.verbose_name


urlpatterns = [
    path('', view=MoviePanelView.as_view(), name='home'),
    path('<slug:moviepanel_slug>', view=MoviePanelView.as_view(), name='panel'),
    path('<slug:moviepanel_slug>/<slug:moviecategory_slug>', view=MovieCategoryView.as_view(), name='category'),
]
