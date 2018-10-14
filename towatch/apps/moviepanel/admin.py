from django.contrib import admin
from .models import MoviePanel, MovieGenre, Movie


@admin.register(MoviePanel)
class MoviePanelAdmin(admin.ModelAdmin):
    model = MoviePanel
    readonly_fields = ('slug', )
    # list_display = ('name', 'created', 'modified', )


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    model = MovieGenre
    readonly_fields = ('slug', )
    # list_display = ('name', 'created', 'modified', )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie
    readonly_fields = ('slug', )
    # list_display = ('name', 'created', 'modified', )
