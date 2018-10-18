from django.test import TestCase
from django.urls import reverse, resolve


class MoviePanelUrl(TestCase):
    def setUp(self):
        self.url_list = reverse('moviepanel:moviepanel-list')
        self.url = reverse('moviepanel:moviepanel-detail', kwargs={'slug': 'test-moviepanel'})
        self.resolver_list = resolve('/api/panels/')
        self.resolver = resolve('/api/panels/horror/')

    def test_moviepanel_reverse(self):
        self.assertEqual(self.url_list, '/api/panels/')
        self.assertEqual(self.url, '/api/panels/test-moviepanel/')

    def test_moviepanel_reverse_invalid(self):
        self.assertNotEqual(self.url_list, '/api/movies/')
        self.assertNotEqual(self.url, '/api/panels/moviepanel-123/')

    def test_moviepanel_resolve(self):
        self.assertEqual(self.resolver_list.view_name, 'moviepanel:moviepanel-list')
        self.assertEqual(self.resolver.view_name, 'moviepanel:moviepanel-detail')

    def test_moviepanel_resolve_invalid(self):
        self.assertNotEqual(self.resolver_list.view_name, 'moviepanel:moviegenre-list')
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:moviegenre-detail')


class MovieGenreUrl(TestCase):
    def setUp(self):
        self.url_list = reverse('moviepanel:moviegenre-list')
        self.url = reverse('moviepanel:moviegenre-detail', kwargs={'slug': 'horror'})
        self.resolver_list = resolve('/api/genres/')
        self.resolver = resolve('/api/genres/horror/')

    def test_moviegenre_reverse(self):
        self.assertEqual(self.url_list, '/api/genres/')
        self.assertEqual(self.url, '/api/genres/horror/')

    def test_moviegenre_reverse_invalid(self):
        self.assertNotEqual(self.url_list, '/api/movies/')
        self.assertNotEqual(self.url, '/api/genres/moviegenre-123/')

    def test_moviegenre_resolve(self):
        self.assertEqual(self.resolver_list.view_name, 'moviepanel:moviegenre-list')
        self.assertEqual(self.resolver.view_name, 'moviepanel:moviegenre-detail')

    def test_moviegenre_resolve_invalid(self):
        self.assertNotEqual(self.resolver_list.view_name, 'moviepanel:moviepanel-list')
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:moviepanel-detail')


class MovieUrl(TestCase):
    def setUp(self):
        self.url_list = reverse('moviepanel:movie-list')
        self.url = reverse('moviepanel:movie-detail', kwargs={'pk': 1})
        self.resolver_list = resolve('/api/movies/')
        self.resolver = resolve('/api/movies/test-movie/')

    def test_movie_reverse(self):
        self.assertEqual(self.url_list, '/api/movies/')
        self.assertEqual(self.url, '/api/movies/1/')

    def test_movie_reverse_invalid(self):
        self.assertNotEqual(self.url_list, '/api/genres/')
        self.assertNotEqual(self.url, '/api/movies/123/')

    def test_movie_resolve(self):
        self.assertEqual(self.resolver_list.view_name, 'moviepanel:movie-list')
        self.assertEqual(self.resolver.view_name, 'moviepanel:movie-detail')

    def test_movie_resolve_invalid(self):
        self.assertNotEqual(self.resolver_list.view_name, 'moviepanel:moviegenre-list')
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:moviegenre-detail')
