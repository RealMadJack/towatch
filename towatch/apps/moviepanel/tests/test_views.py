from django.test import Client, TestCase
from django.urls import reverse

from ..models import MoviePanel, MovieCategory


class MoviePanelView(TestCase):
    def setUp(self):
        self.client = Client()
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.response = self.client.get(
            reverse('moviepanel:panel', kwargs={'moviepanel_slug': self.moviepanel.slug}))

    def test_moviepanel_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_moviepanel_response_invalid(self):
        self.assertNotEqual(self.response.status_code, 404)

    def test_moviepanel_content(self):
        self.assertNotEqual('{}', self.response.content.decode('utf-8'))
        self.assertIn(self.moviepanel.name, self.response.content.decode('utf-8'))

    def test_moviepanel_content_invalid(self):
        self.assertNotIn('stringendo', self.response.content.decode('utf-8'))


class MovieCategoryView(TestCase):
    def setUp(self):
        self.client = Client()
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviecategory = MovieCategory.objects.create(name='test category', moviepanel=self.moviepanel)
        self.response = self.client.get(reverse('moviepanel:category', kwargs={
                                        'moviepanel_slug': self.moviepanel.slug,
                                        'moviecategory_slug': self.moviecategory.slug}))

    def test_moviecategory_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_moviecategory_response_invalid(self):
        self.assertNotEqual(self.response.status_code, 404)

    def test_moviecategory_content(self):
        self.assertNotEqual('{}', self.response.content.decode('utf-8'))
        self.assertIn(self.moviecategory.name, self.response.content.decode('utf-8'))

    def test_moviecategory_content_invalid(self):
        self.assertNotIn('stringendo', self.response.content.decode('utf-8'))
