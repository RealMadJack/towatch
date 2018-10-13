from django.test import TestCase
from django.urls import reverse

from ..models import MoviePanel, MovieCategory


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


class MovieCategoryModel(TestCase):
    def setUp(self):
        self.moviepanel = MoviePanel.objects.create(name='test panel')
        self.moviecategory = MovieCategory.objects.create(name='test category', moviepanel=self.moviepanel)

    def test_moviepanel_data(self):
        self.assertEqual(self.moviecategory.name, 'test category')
        self.assertEqual(self.moviecategory.slug, 'test-category')
        self.assertEqual(self.moviecategory.moviepanel.name, 'test panel')

    def test_moviepanel_data_invalid(self):
        self.assertNotEqual(self.moviecategory.name, 'test cat 1')
        self.assertNotEqual(self.moviecategory.slug, 'not_123')
        self.assertNotEqual(self.moviecategory.moviepanel.name, 'incorrect')

    def test_moviecategory_absolute_url(self):
        abs_url = self.moviecategory.get_absolute_url()
        reverse_url = reverse('moviepanel:category', kwargs={
            'moviepanel_slug': self.moviecategory.moviepanel.slug,
            'moviecategory_slug': self.moviecategory.slug,
        })
        self.assertEqual(abs_url, reverse_url)

    def test_moviecategory_absolute_url_invalid(self):
        abs_url = self.moviecategory.get_absolute_url()
        self.assertNotEqual(abs_url, '123')

    def test_moviecategory_save_unique_slug(self):
        self.assertEqual(self.moviecategory.slug, 'test-category')
        self.moviecategory.name = 'test new category'
        self.moviecategory.save()
        self.assertEqual(self.moviecategory.slug, 'test-new-category')

    def test_moviecategory_save_unique_slug_invalid(self):
        self.assertEqual(self.moviecategory.slug, 'test-category')
        self.moviecategory.name = 'test new category'
        self.moviecategory.save()
        self.assertNotEqual(self.moviecategory.slug, 'test-new-category-1')
