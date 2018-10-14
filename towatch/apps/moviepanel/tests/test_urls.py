from django.test import TestCase
from django.urls import reverse, resolve


class MoviePanelUrl(TestCase):
    def setUp(self):
        self.url = reverse('moviepanel:panel', kwargs={'moviepanel_slug': 'test-moviepanel'})
        self.resolver = resolve('/api/test-moviepanel')

    def test_moviepanel_reverse(self):
        self.assertEqual(self.url, '/api/test-moviepanel')

    def test_moviepanel_reverse_invalid(self):
        self.assertNotEqual(self.url, '/api/test-moviepanel-123')

    def test_moviepanel_resolve(self):
        self.assertEqual(self.resolver.view_name, 'moviepanel:panel')

    def test_moviepanel_resolve_invalid(self):
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:genre')


class MovieGenreUrl(TestCase):
    def setUp(self):
        self.url = reverse('moviepanel:genre', kwargs={
                           'moviepanel_slug': 'moviepanel',
                           'moviegenre_slug': 'moviegenre'})
        self.resolver = resolve('/api/moviepanel/movie-genre')

    def test_moviegenre_reverse(self):
        self.assertEqual(self.url, '/api/moviepanel/moviegenre')

    def test_moviegenre_reverse_invalid(self):
        self.assertNotEqual(self.url, '/api/moviepanel/moviegenre-123')

    def test_moviepanel_resolve(self):
        self.assertEqual(self.resolver.view_name, 'moviepanel:genre')

    def test_moviepanel_resolve_invalid(self):
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:panel')
