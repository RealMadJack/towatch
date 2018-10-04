from django.urls import path

from .apps import MoviepanelConfig
from .views import MoviePanelView

app_name = MoviepanelConfig.verbose_name


urlpatterns = [
    path('<slug:moviepanel_slug>', view=MoviePanelView.as_view(), name='home'),
]
