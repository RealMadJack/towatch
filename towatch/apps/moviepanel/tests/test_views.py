from django.test import Client, TestCase
from django.urls import reverse

from ..models import MoviePanel, MovieGenre, Movie


class MoviePanelView(TestCase):
    def setUp(self):
        self.client = Client()
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviegenre = MovieGenre.objects.create(name='test genre', moviepanel=self.moviepanel)
        self.movie = Movie.objects.create(name='test movie', description='test description',
                                          moviepanel=self.moviepanel)
        self.movie.moviegenre.add(self.moviegenre)
        self.response_list = self.client.get(reverse('moviepanel:moviepanel-list'))
        self.response = self.client.get(
            reverse('moviepanel:moviepanel-detail', kwargs={'slug': self.moviepanel.slug}))

    def test_moviepanel_response(self):
        self.assertEqual(self.response_list.status_code, 200)
        self.assertEqual(self.response.status_code, 200)

    def test_moviepanel_response_invalid(self):
        self.assertNotEqual(self.response_list.status_code, 404)
        self.assertNotEqual(self.response.status_code, 404)

    def test_moviepanel_content(self):
        self.assertIn(self.moviepanel.name, self.response_list.content.decode('utf-8'))
        self.assertIn('moviegenres', self.response_list.content.decode('utf-8'))
        self.assertIn('moviegenre', self.response_list.content.decode('utf-8'))
        self.assertIn('movies', self.response_list.content.decode('utf-8'))
        self.assertIn(self.moviepanel.name, self.response.content.decode('utf-8'))
        self.assertIn('moviegenres', self.response.content.decode('utf-8'))
        self.assertIn('moviegenre', self.response.content.decode('utf-8'))
        self.assertIn('movies', self.response.content.decode('utf-8'))

    def test_moviepanel_content_invalid(self):
        self.assertNotEqual('{}', self.response_list.content.decode('utf-8'))
        self.assertNotEqual('{}', self.response.content.decode('utf-8'))


class MovieGenreView(TestCase):
    def setUp(self):
        self.client = Client()
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviegenre = MovieGenre.objects.create(name='test genre', moviepanel=self.moviepanel)
        self.movie = Movie.objects.create(name='test movie', description='test description',
                                          moviepanel=self.moviepanel)
        self.movie.moviegenre.add(self.moviegenre)
        self.response_list = self.client.get(reverse('moviepanel:moviegenre-list'))
        self.response = self.client.get(
            reverse('moviepanel:moviegenre-detail', kwargs={'slug': self.moviegenre.slug}))

    def test_moviegenre_response(self):
        self.assertEqual(self.response_list.status_code, 200)
        self.assertEqual(self.response.status_code, 200)

    def test_moviegenre_response_invalid(self):
        self.assertNotEqual(self.response_list.status_code, 404)
        self.assertNotEqual(self.response.status_code, 404)

    def test_moviegenre_content(self):
        self.assertIn(self.moviegenre.name, self.response_list.content.decode('utf-8'))
        self.assertIn('moviepanel', self.response_list.content.decode('utf-8'))
        self.assertIn('movies', self.response_list.content.decode('utf-8'))
        self.assertIn(self.moviegenre.name, self.response.content.decode('utf-8'))
        self.assertIn('moviepanel', self.response.content.decode('utf-8'))
        self.assertIn('movies', self.response.content.decode('utf-8'))

    def test_moviegenre_content_invalid(self):
        self.assertNotEqual('{}', self.response_list.content.decode('utf-8'))
        self.assertNotEqual('{}', self.response.content.decode('utf-8'))


class MovieView(TestCase):
    def setUp(self):
        self.client = Client()
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviegenre = MovieGenre.objects.create(name='test genre', moviepanel=self.moviepanel)
        self.movie = Movie.objects.create(name='test movie', description='test description',
                                          moviepanel=self.moviepanel)
        self.movie.moviegenre.add(self.moviegenre)
        self.response_list = self.client.get(reverse('moviepanel:movie-list'))
        self.response = self.client.get(
            reverse('moviepanel:movie-detail', kwargs={'pk': self.movie.pk}))

    def test_movie_response(self):
        self.assertEqual(self.response_list.status_code, 200)
        self.assertEqual(self.response.status_code, 200)

    def test_movie_response_invalid(self):
        self.assertNotEqual(self.response_list.status_code, 404)
        self.assertNotEqual(self.response.status_code, 404)

    def test_movie_content(self):
        self.assertIn(self.movie.name, self.response_list.content.decode('utf-8'))
        self.assertIn('moviepanel', self.response_list.content.decode('utf-8'))
        self.assertIn('moviegenre', self.response_list.content.decode('utf-8'))
        self.assertIn(self.movie.name, self.response.content.decode('utf-8'))
        self.assertIn('moviepanel', self.response.content.decode('utf-8'))
        self.assertIn('moviegenre', self.response.content.decode('utf-8'))

    def test_movie_content_invalid(self):
        self.assertNotEqual('{}', self.response_list.content.decode('utf-8'))
        self.assertNotEqual('{}', self.response.content.decode('utf-8'))
