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
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:category')


class MovieCategoryUrl(TestCase):
    def setUp(self):
        self.url = reverse('moviepanel:category', kwargs={
                           'moviepanel_slug': 'moviepanel',
                           'moviecategory_slug': 'moviecategory'})
        self.resolver = resolve('/api/moviepanel/movie-category')

    def test_moviecategory_reverse(self):
        self.assertEqual(self.url, '/api/moviepanel/moviecategory')

    def test_moviecategory_reverse_invalid(self):
        self.assertNotEqual(self.url, '/api/moviepanel/moviecategory-123')

    def test_moviepanel_resolve(self):
        self.assertEqual(self.resolver.view_name, 'moviepanel:category')

    def test_moviepanel_resolve_invalid(self):
        self.assertNotEqual(self.resolver.view_name, 'moviepanel:panel')
