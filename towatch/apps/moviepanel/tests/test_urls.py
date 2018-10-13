from django.urls import reverse, resolve
from django.test import Client, TestCase


class MoviePanelUrl(TestCase):
    def setUp(self):
        self.client = Client()

    def test_moviepanel_reverse(self):
        self.assertEqual(
            reverse('moviepanel:panel', kwargs={'moviepanel_slug': 'test-moviepanel'}),
            '/api/test-moviepanel'
        )

    def test_moviepanel_invalid_reverse(self):
        self.assertNotEqual(
            reverse('moviepanel:panel', kwargs={'moviepanel_slug': 'test-moviepanel'}),
            '/test-moviepanel-123'
        )


class MovieCategoryModel(TestCase):
    def setUp(self):
        self.client = Client()
