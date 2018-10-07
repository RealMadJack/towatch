from django.test import TestCase
from django.urls import reverse

from ..models import MoviePanel


class MoviePanelModel(TestCase):
    def setUp(self):
        self.moviepanel = MoviePanel(name='test panel')
        self.moviepanel.save()
        self.moviepanel_1 = MoviePanel(name='test panel')
        self.moviepanel_1.save()

    def test_moviepanel_absolute_url(self):
        abs_url = self.moviepanel.get_absolute_url()
        abs_url_1 = self.moviepanel_1.get_absolute_url()
        reverse_url = reverse('moviepanel:panel', kwargs={
            'moviepanel_slug': self.moviepanel.slug})
        reverse_url_1 = reverse('moviepanel:panel', kwargs={
            'moviepanel_slug': self.moviepanel_1.slug})

        self.assertEqual(abs_url, reverse_url)
        self.assertEqual(abs_url_1, reverse_url_1)

    def test_moviepanel_save_unique_slug(self):
        self.assertEqual(self.moviepanel.slug, 'test-panel')
        self.assertEqual(self.moviepanel_1.slug, 'test-panel-1')

        self.moviepanel.name = 'test new panel'
        self.moviepanel.save()
        self.moviepanel_1.name = 'test new panel'
        self.moviepanel_1.save()
        self.assertEqual(self.moviepanel.slug, 'test-new-panel')
        self.assertEqual(self.moviepanel_1.slug, 'test-new-panel-1')
