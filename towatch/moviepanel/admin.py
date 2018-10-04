from django.contrib import admin
from .models import MoviePanel, MovieCategory, Movie


@admin.register(MoviePanel)
class MoviePanelAdmin(admin.ModelAdmin):
    model = MoviePanel
    readonly_fields = ('slug', )
    # list_display = ('name', 'created', 'modified', )
