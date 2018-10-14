from django.test import TestCase
from django.urls import reverse

from ..models import MoviePanel, MovieGenre, Movie


class MoviePanelModel(TestCase):
    def setUp(self):
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviepanel_1 = MoviePanel.objects.create(name='test panel')

    def test_moviepanel_data(self):
        self.assertEqual(self.moviepanel.name, 'test panel')
        self.assertEqual(self.moviepanel.slug, 'test-panel')
        self.assertEqual(self.moviepanel_1.name, 'test panel')
        self.assertEqual(self.moviepanel_1.slug, 'test-panel-1')

    def test_moviepanel_data_invalid(self):
        self.assertNotEqual(self.moviepanel.name, 'test panel 1')
        self.assertNotEqual(self.moviepanel.slug, 'not')
        self.assertNotEqual(self.moviepanel_1.name, 'test panel 2')
        self.assertNotEqual(self.moviepanel_1.slug, 'test-panel_1')

    def test_moviepanel_absolute_url(self):
        abs_url = self.moviepanel.get_absolute_url()
        abs_url_1 = self.moviepanel_1.get_absolute_url()
        reverse_url = reverse('moviepanel:panel', kwargs={
            'moviepanel_slug': self.moviepanel.slug})
        reverse_url_1 = reverse('moviepanel:panel', kwargs={
            'moviepanel_slug': self.moviepanel_1.slug})

        self.assertEqual(abs_url, reverse_url)
        self.assertEqual(abs_url_1, reverse_url_1)

    def test_moviepanel_absolute_url_invalid(self):
        abs_url = self.moviepanel.get_absolute_url()
        self.assertNotEqual(abs_url, '123')

    def test_moviepanel_save_unique_slug(self):
        self.assertEqual(self.moviepanel.slug, 'test-panel')
        self.assertEqual(self.moviepanel_1.slug, 'test-panel-1')
        self.moviepanel.name = 'test new panel'
        self.moviepanel.save()
        self.moviepanel_1.name = 'test new panel'
        self.moviepanel_1.save()
        self.assertEqual(self.moviepanel.slug, 'test-new-panel')
        self.assertEqual(self.moviepanel_1.slug, 'test-new-panel-1')

    def test_moviepanel_save_unique_slug_invalid(self):
        self.assertEqual(self.moviepanel.slug, 'test-panel')
        self.assertEqual(self.moviepanel_1.slug, 'test-panel-1')
        self.moviepanel.name = 'test new panel'
        self.moviepanel.save()
        self.moviepanel_1.name = 'test new panel'
        self.moviepanel_1.save()
        self.assertNotEqual(self.moviepanel.slug, 'test-panel')
        self.assertNotEqual(self.moviepanel_1.slug, 'test-panel-1')


class MovieGenreModel(TestCase):
    def setUp(self):
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviegenre = MovieGenre.objects.create(name='test genre', moviepanel=self.moviepanel)

    def test_moviepanel_data(self):
        self.assertEqual(self.moviegenre.name, 'test genre')
        self.assertEqual(self.moviegenre.slug, 'test-genre')
        self.assertEqual(self.moviegenre.moviepanel.name, 'test panel')

    def test_moviepanel_data_invalid(self):
        self.assertNotEqual(self.moviegenre.name, 'test cat 1')
        self.assertNotEqual(self.moviegenre.slug, 'not_123')
        self.assertNotEqual(self.moviegenre.moviepanel.name, 'incorrect')

    def test_moviegenre_absolute_url(self):
        abs_url = self.moviegenre.get_absolute_url()
        reverse_url = reverse('moviepanel:genre', kwargs={
            'moviepanel_slug': self.moviegenre.moviepanel.slug,
            'moviegenre_slug': self.moviegenre.slug,
        })
        self.assertEqual(abs_url, reverse_url)

    def test_moviegenre_absolute_url_invalid(self):
        abs_url = self.moviegenre.get_absolute_url()
        self.assertNotEqual(abs_url, '123')

    def test_moviegenre_save_unique_slug(self):
        self.assertEqual(self.moviegenre.slug, 'test-genre')
        self.moviegenre.name = 'test new genre'
        self.moviegenre.save()
        self.assertEqual(self.moviegenre.slug, 'test-new-genre')

    def test_moviegenre_save_unique_slug_invalid(self):
        self.assertEqual(self.moviegenre.slug, 'test-genre')
        self.moviegenre.name = 'test new genre'
        self.moviegenre.save()
        self.assertNotEqual(self.moviegenre.slug, 'test-new-genre-1')


class MovieModel(TestCase):
    def setUp(self):
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.movie = Movie.objects.create(name='test movie', description='test description', moviepanel=self.moviepanel)

    def test_moviepanel_data(self):
        self.assertEqual(self.movie.name, 'test movie')
        self.assertEqual(self.movie.description, 'test description')
        self.assertEqual(self.movie.slug, 'test-movie')
        self.assertEqual(self.movie.moviepanel.name, 'test panel')

    def test_moviepanel_data_invalid(self):
        self.assertNotEqual(self.movie.name, 'test cat 1')
        self.assertNotEqual(self.movie.description, 'lorem ipsum')
        self.assertNotEqual(self.movie.slug, 'not_123')
        self.assertNotEqual(self.movie.moviepanel.name, 'incorrect')

    def test_movie_absolute_url(self):
        abs_url = self.movie.get_absolute_url()
        reverse_url = reverse('moviepanel:movie', kwargs={
            'moviepanel_slug': self.movie.moviepanel.slug,
            'movie_slug': self.movie.slug,
        })
        self.assertEqual(abs_url, reverse_url)

    def test_movie_absolute_url_invalid(self):
        abs_url = self.movie.get_absolute_url()
        self.assertNotEqual(abs_url, '123')

    def test_movie_save_unique_slug(self):
        self.assertEqual(self.movie.slug, 'test-movie')
        self.movie.name = 'test new movie'
        self.movie.save()
        self.assertEqual(self.movie.slug, 'test-new-movie')

    def test_movie_save_unique_slug_invalid(self):
        self.assertEqual(self.movie.slug, 'test-movie')
        self.movie.name = 'test new movie'
        self.movie.save()
        self.assertNotEqual(self.movie.slug, 'test-new-movie-1')
