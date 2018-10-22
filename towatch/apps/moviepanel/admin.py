from django.contrib import admin
from .models import MoviePanel, MovieGenre, Movie


@admin.register(MoviePanel)
class MoviePanelAdmin(admin.ModelAdmin):
    model = MoviePanel
    readonly_fields = ('slug', )
    list_display = ('name', 'created', 'modified', )


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    model = MovieGenre
    readonly_fields = ('slug', )
    list_display = ('name', 'get_moviepanel', 'created', 'modified', )

    def get_moviepanel(self, obj):
        return obj.moviepanel.name
    get_moviepanel.short_description = 'Movie Panel'
    get_moviepanel.admin_order_field = 'moviepanel'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie
    readonly_fields = ('slug', )
    filter_horizontal = ('moviegenre', )
    list_display = ('name', 'get_moviepanel', 'created', 'modified', )

    def get_moviepanel(self, obj):
        return obj.moviepanel.name
    get_moviepanel.short_description = 'Movie Panel'
    get_moviepanel.admin_order_field = 'moviepanel'
