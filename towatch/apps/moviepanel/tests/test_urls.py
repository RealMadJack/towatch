from django.test import TestCase
from django.urls import reverse, resolve


class MoviePanelUrl(TestCase):
    def setUp(self):
        self.url = reverse('moviepanel:panel', kwargs={'moviepanel_slug': 'test-moviepanel'})
        self.resolver = resolve('/api/test-moviepanel/')

    def test_moviepanel_reverse(self):
        self.assertEqual(self.url, '/api/test-moviepanel/')

    def test_moviepanel_reverse_invalid(self):
        self.assertNotEqual(self.url, '/api/test-moviepanel-123/')

    def test_moviepanel_resolve(self):
        self.assertEqual(self.resolver.view_name, 'moviepanel:panel')

    def test_moviepanel_resolve_invalid(self):
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:genre')


class MovieGenreUrl(TestCase):
    def setUp(self):
        self.url = reverse('moviepanel:genre', kwargs={
                           'moviepanel_slug': 'moviepanel',
                           'moviegenre_slug': 'moviegenre'})
        self.resolver = resolve('/api/moviepanel/genres/movie-genre/')

    def test_moviegenre_reverse(self):
        self.assertEqual(self.url, '/api/moviepanel/genres/moviegenre/')

    def test_moviegenre_reverse_invalid(self):
        self.assertNotEqual(self.url, '/api/moviepanel/genres/moviegenre-123/')

    def test_moviegenre_resolve(self):
        self.assertEqual(self.resolver.view_name, 'moviepanel:genre')

    def test_moviegenre_resolve_invalid(self):
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:panel')


class MovieUrl(TestCase):
    def setUp(self):
        self.url = reverse('moviepanel:movie', kwargs={
                           'moviepanel_slug': 'moviepanel',
                           'movie_slug': 'movie'})
        self.resolver = resolve('/api/moviepanel/movie/')

    def test_movie_reverse(self):
        self.assertEqual(self.url, '/api/moviepanel/movie/')

    def test_movie_reverse_invalid(self):
        self.assertNotEqual(self.url, '/api/moviepanel/movie-123/')

    # def test_movie_resolve(self):
    #     self.assertEqual(self.resolver.view_name, 'moviepanel:movie')

    # def test_movie_resolve_invalid(self):
    #     self.assertNotEqual(self.resolver.view_name, 'moviepanel:panel')
