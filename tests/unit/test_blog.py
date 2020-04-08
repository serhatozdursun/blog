from unittest import TestCase
from blog import Blog

b = Blog('Test', 'Test Author')


class BlogTest(TestCase):

    def test_create_blog(self):
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_rper(self):
        b2 = Blog('Benim günüm', 'Serhat')
        self.assertEqual(b.__repr__(), 'Test by Test Author(0 post)')
        self.assertEqual(b2.__repr__(), 'Benim günüm by Serhat(0 post)')

    def test_repr_multiple_posts(self):
        b.posts = ['Test']

        b2 = Blog('Quarintina Week Ends', 'Serhat')
        b2.posts = ['Test', 'another']
        self.assertEqual(b.__repr__(), 'Test by Test Author(1 post)')
        self.assertEqual(b2.__repr__(), 'Quarintina Week Ends by Serhat(2 posts)')

