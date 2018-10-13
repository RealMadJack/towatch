from django.test import TestCase


class MoviePanelView(TestCase):
    pass


class MovieCategoryView(TestCase):
    def setUp(self):
        pass

    # def test_user_can_read(self):
    #     """
    #     Tests that a user is allowed to read.
    #     """
    #     self.c.login(username='newsposter', password='newspass')
    #     response = self.c.get('/news/get_post/1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotEqual(response.content, '{}')
