# -*- coding: utf-8 -*-
import time

BLOG_AUTHOR = 'Python Floripa'
BLOG_TITLE = 'Python Floripa'
BLOG_EMAIL = 'pythonflorianopolis@gmail.com'
BLOG_DESCRIPTION = 'Site da comunidade Python Floripa!'

DEFAULT_LANG = 'pt_br'

SITE_URL = 'http://floripa.sc.python.org.br/'
BASE_URL = 'http://pythonfloripa.github.io/'
PRETTY_URLS = True

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/', 'Início'),
        ('/contato/', 'Contato'),
        ('https://floripa.sc.python.org.br/v1/', 'Site Original'),
    ),
}

POSTS = (
    ('posts/*.md', 'posts', 'post.tmpl'),
)
PAGES = (
    ('pages/*.md', '', 'page.tmpl'),
)
INDEX_PATH = 'pages/inicio.md'

THEME = 'python-floripa'
THEME_CONFIG = {
    DEFAULT_LANG: {
        'navbar_light': False,
        'navbar_custom_bg': 'bg-python-floripa',
    }
}
EXTRA_HEAD_DATA = '''
<link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet">
'''
SHOW_SOURCELINK = False
CODE_COLOR_SCHEME = 'paraiso-dark'

OUTPUT_FOLDER = 'saida-nikola'
CACHE_FOLDER = 'cache'

TIMEZONE = 'America/Sao_Paulo'
DATE_FORMAT = 'dd/MM/yyyy HH:mm'
LUXON_DATE_FORMAT = {
    DEFAULT_LANG: {'preset': False, 'format': DATE_FORMAT},
}

COMPILERS = {
    'markdown': ['.md', '.mdown', '.markdown'],
    'html': ['.html', '.htm'],
}

METADATA_FORMAT = 'Nikola'
ONE_FILE_POSTS = False
FILE_METADATA_UNSLUGIFY_TITLES = True

IMAGE_FOLDERS = {'images': 'images'}
DEFAULT_PREVIEW_IMAGE = '/images/CAPA_PYTHON_FLORIPA.png'
LOGO_URL = '/images/LOGO_PYTHON_FLORIPA_HORIZONTAL.svg'
SHOW_BLOG_TITLE = False

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
FAVICONS = (
    ('icon', '/images/LOGO_PYTHON_FLORIPA.svg', '16x16'),
    # ('icon', '/favicon.ico', '16x16'),
    # ('icon', '/icon_128x128.png', '128x128'),
)

GITHUB_SOURCE_BRANCH = 'development'
GITHUB_DEPLOY_BRANCH = 'master'
GITHUB_REMOTE_NAME = 'origin'
GITHUB_COMMIT_SOURCE = True

LICENSE = '''
<a rel="license" href="
https://github.com/PythonFloripa/pythonfloripa.github.io/blob/development/LICENSE
">Licença MIT</a>
'''

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            'email': BLOG_EMAIL,
            'author': BLOG_AUTHOR,
            'date': time.gmtime().tm_year,
            'license': LICENSE
        }
    )
}
CONTENT_FOOTER = '''
&copy; {date} <a href="mailto:{email}">{author}</a> |
Produzido com <a href="https://getnikola.com" rel="nofollow">Nikola</a>
'''

MARKDOWN_EXTENSIONS = [
    'markdown.extensions.fenced_code',
    'markdown.extensions.codehilite',
    'markdown.extensions.extra'
]
