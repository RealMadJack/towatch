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
        self.moviepanel_1 = MoviePanel.objects.create(name='movies')
        self.moviegenre = MovieGenre.objects.create(name='horror', moviepanel=self.moviepanel)
        self.moviegenre_1 = MovieGenre.objects.create(name='comedy', moviepanel=self.moviepanel)
        self.moviegenre_2 = MovieGenre.objects.create(name='action', moviepanel=self.moviepanel_1)
        self.movie = Movie.objects.create(name='test movie', description='test description', moviepanel=self.moviepanel)
        self.movie_1 = Movie.objects.create(name='kill bill', description='blood bath', moviepanel=self.moviepanel_1)
        self.movie.moviegenre.add(self.moviegenre, self.moviegenre_1)
        self.movie_1.moviegenre.add(self.moviegenre, self.moviegenre_1, self.moviegenre_2)

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

    def test_movie_status(self):
        self.assertEqual(self.movie.status, 'invisible')
        self.movie.status = self.movie.STATUS['visible']
        self.movie.save()
        self.assertEqual(self.movie.status, 'visible')

    def test_movie_status_invalid(self):
        self.assertNotEqual(self.movie.status, 'visible')
        self.assertNotEqual(self.movie.status, '')

    def test_movie_moviegenre_m2m(self):
        # m2m add test
        moviegenre_list = list(self.movie.moviegenre.all())
        moviegenre_list_1 = list(self.movie_1.moviegenre.all())
        self.assertEqual(len(moviegenre_list), 2)
        self.assertEqual(len(moviegenre_list_1), 3)
        self.assertEqual(moviegenre_list[0].name, 'horror')
        self.assertEqual(moviegenre_list[-1].name, 'comedy')
        self.assertEqual(moviegenre_list_1[0].name, 'horror')
        self.assertEqual(moviegenre_list_1[-1].name, 'action')
        # m2m remove test
        self.movie.moviegenre.remove(moviegenre_list[0])
        self.movie_1.moviegenre.remove(moviegenre_list[0])
        moviegenre_list = list(self.movie.moviegenre.all())
        moviegenre_list_1 = list(self.movie_1.moviegenre.all())
        self.assertEqual(len(moviegenre_list), 1)
        self.assertEqual(len(moviegenre_list_1), 2)
        self.assertEqual(moviegenre_list[0].name, 'comedy')
        self.assertEqual(moviegenre_list_1[0].name, 'comedy')

    def test_movie_moviegenre_m2m_invalid(self):
        moviegenre_list = self.movie.moviegenre.all()
        moviegenre_list_1 = self.movie_1.moviegenre.all()
        self.assertNotEqual(len(moviegenre_list), 0)
        self.assertNotEqual(len(moviegenre_list_1), 0)
        self.assertNotEqual(moviegenre_list[0].name, '')
        self.assertNotEqual(moviegenre_list_1[0].name, '')
        self.movie.moviegenre.remove(moviegenre_list[0])
        self.movie_1.moviegenre.remove(moviegenre_list[0])
        # m2m remove test
        moviegenre_list = list(self.movie.moviegenre.all())
        moviegenre_list_1 = list(self.movie_1.moviegenre.all())
        self.assertNotEqual(len(moviegenre_list), 2)
        self.assertNotEqual(len(moviegenre_list_1), 3)
        self.assertNotEqual(moviegenre_list[0].name, 'horror')
        self.assertNotEqual(moviegenre_list_1[0].name, 'horror')

    def test_moviegenre_movie_m2m_reverse(self):
        # m2m add test
        movie_list = list(self.moviegenre.movies.all())
        movie_list_1 = list(self.moviegenre_1.movies.all())
        movie_list_2 = list(self.moviegenre_2.movies.all())
        self.assertEqual(len(movie_list), 2)
        self.assertEqual(len(movie_list_1), 2)
        self.assertEqual(len(movie_list_2), 1)
        self.assertEqual(movie_list[0].name, 'kill bill')
        self.assertEqual(movie_list[-1].name, 'test movie')
        self.assertEqual(movie_list_2[0].name, 'kill bill')
        self.assertEqual(movie_list_2[-1].name, 'kill bill')

    def test_moviegenre_movie_m2m_reverse_invalid(self):
        # m2m add test
        movie_list = list(self.moviegenre.movies.all())
        movie_list_1 = list(self.moviegenre_1.movies.all())
        movie_list_2 = list(self.moviegenre_2.movies.all())
        self.assertNotEqual(len(movie_list), 0)
        self.assertNotEqual(len(movie_list_1), 0)
        self.assertNotEqual(len(movie_list_2), 0)
        self.assertNotEqual(movie_list[0].name, '')
        self.assertNotEqual(movie_list_1[0].name, '')
        self.assertNotEqual(movie_list_2[0].name, '')
