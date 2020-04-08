from blog import Blog
from post import Post

blogs = dict()

MENUE_PROMT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or ' ' to quit: "

POST_TAMPLATE = '''
    ---{}---
    {}
    '''


def menue():
    # show the user available blogs
    # let the user make choice
    # Do something with that choice

    print_blogs()
    selection = input(MENUE_PROMT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_create_post()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENUE_PROMT)


def print_blogs():
    for blog, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    title = input('Enter your blog title')
    author = input('Enter youre blog author')
    blogs[title] = Blog(title, author)


def ask_create_post():
    blog_name = input('Enter your blog title: ')
    title =  input('Enter your post title: ')
    content = input('Enter youre post content')
    blogs[blog_name].create_post(title,content)

def print_post(post):
    print(POST_TAMPLATE.format(post.title, post.content))


def print_posts(blogs):
    for post in blogs.posts:
        print_post(post)


def ask_read_blog():
    title = input('Enter the bllog title you want to read: ')
    print_posts(blogs[title])
