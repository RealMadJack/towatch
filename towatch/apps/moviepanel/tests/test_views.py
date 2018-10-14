from django.test import Client, TestCase
from django.urls import reverse

from ..models import MoviePanel, MovieGenre


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


class MovieGenreView(TestCase):
    def setUp(self):
        self.client = Client()
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviegenre = MovieGenre.objects.create(name='test genre', moviepanel=self.moviepanel)
        self.response = self.client.get(reverse('moviepanel:genre', kwargs={
                                        'moviepanel_slug': self.moviepanel.slug,
                                        'moviegenre_slug': self.moviegenre.slug}))

    def test_moviegenre_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_moviegenre_response_invalid(self):
        self.assertNotEqual(self.response.status_code, 404)

    def test_moviegenre_content(self):
        self.assertNotEqual('{}', self.response.content.decode('utf-8'))
        self.assertIn(self.moviegenre.name, self.response.content.decode('utf-8'))

    def test_moviegenre_content_invalid(self):
        self.assertNotIn('stringendo', self.response.content.decode('utf-8'))
