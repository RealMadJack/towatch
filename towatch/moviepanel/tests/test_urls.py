from django.urls import reverse, resolve
from django.test import Client, TestCase


class MoviePanelTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_moviepanel_reverse(self):
        self.assertEqual(
            reverse('moviepanel:home', kwargs={'moviepanel_slug': 'test-moviepanel'}),
            '/test-moviepanel'
        )

    def test_moviepanel_invalid_reverse(self):
        self.assertNotEqual(
            reverse('moviepanel:home', kwargs={'moviepanel_slug': 'test-moviepanel'}),
            '/test-moviepanel-123'
        )

    def test_moviepanel_resolve(self):
        self.assertEqual(resolve('/test-movieboard-slug').view_name, 'moviepanel:home')
