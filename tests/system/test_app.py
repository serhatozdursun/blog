from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_menue_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menue()
                mocked_print_blogs.assert_called()

    def test_menu_prints_promt(self):
        with patch('builtins.input') as mocked_input:
            app.menue()
            mocked_input.assert_called_with(app.MENUE_PROMT)

    def test_print_blpgs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author(0 post)')

    def test_ask_create_blogs(self):
        with patch('builtins.input', return_value='Test') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_create_post(self):
        blog = app.blogs['Test']
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test', 'Test Content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected_print = app.POST_TAMPLATE.format(post.title, post.content)
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = app.blogs['Test']

        with patch('builtins.input', ) as mocked_input:
            mocked_input.side_effect = ('Test', 'Post title', 'Post Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Post title')
            self.assertEqual(blog.posts[0].content, 'Post Content')

    def test_menue_called_asked_create_blog(self):
        with patch('builtins.input') as mocked_import:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_import.side_effect = ('c', "q")
                app.menue()
                mocked_ask_create_blog.assert_called()

    def test_menue_called_print_blogs(self):
        with patch('builtins.input') as mocked_import:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_import.side_effect = ('l', "q")
                app.menue()
                self.assertEqual(mocked_print_blogs.call_count, 2)

    def test_menue_called_ask_create_post(self):
        with patch('builtins.input') as mocked_import:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_import.side_effect = ('r', "q")
                app.menue()
                mocked_ask_create_post.assert_called()

    def test_menue_called_ask_create_post(self):
        with patch('builtins.input') as mocked_import:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_import.side_effect = ('r', "q")
                app.menue()
                mocked_ask_create_post.assert_called()
