#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'crazygit'
SITENAME = u'Soul Mate'
SITE_SUBNAME = u'宁静的夜，心中一片静谧'
SITEURL = 'http://localhost/blog'

TIMEZONE = 'Asia/Chongqing'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Use folder as category,  don’t specify a category in your post metadata

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = u'其它'

# URL settings
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'


# pagination settings
DEFAULT_PAGINATION = 10

# theme settings
THEME = 'blog-theme'

# code highlight style
# [default emacs friendly colorful autumn murphy manni
# monokai perldoc pastie borland trac native fruity bw vs tango]
PYGMENT_STYLE = "colorful"
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# CNAME settings
STATIC_PATHS = [
    'extra/CNAME',
    'extra/README.md',
    'extra/robots.txt',
    ]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README.md': {'path': 'README.md'},
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# ACCOUNT settings
GITHUB_URL = "https://github.com/crazygit"

# DISQUS_SITENAME = 'lianglin999'
BAIDU_SHARE_UID = 5513994
YOUYAN_UID = 1774842
BAIDU_ANALYTICS = '3Fbd2f7fd2b210d56de826c217b8a5a70c'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# feed
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

# Links
LINKS = (
    ("Travis-ci", "https://travis-ci.org/"),
    ("Wercker", "http://wercker.com/"),
    ("Cloudbees", "http://www.cloudbees.com"),
    ("Pelican", "http://docs.getpelican.com/"),
    ("Jinja", "http://jinja.pocoo.org/"),
    ("Bootstrap", "http://www.bootcss.com/"),
)

# plugins
PLUGIN_PATH = 'plugins'
PLUGINS = ['assets', 'cjk-auto-spacing',
           'extract_toc', 'gzip_cache', 'neighbors', 'optimize_images', 'sitemap']


# plugin assets configure
ASSET_SOURCE_PATHS = (
    'static/css',
    'static/pygments',
    )
ASSET_BUNDLES = (
    ('mycss', ['custom.css', PYGMENT_STYLE + '.css'], {'filters': 'cssmin'}),
    )


# plugin extract_toc configure
MD_EXTENSIONS = (['toc'])

# plugin sitemap configure
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
