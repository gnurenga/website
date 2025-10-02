#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'rengaraj'
SITENAME = u'rengaraj'
SITEURL = ''
FAVICON_URL = 'https://www.python.org/static/favicon.ico'
PATH = 'content'

TIMEZONE = 'Asia/Kolkata'


DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sakthirengaraj'),
          ('linkedin', 'https://in.linkedin.com/in/rengaraj-d-1b804a16'),
           ('github', 'https://github.com/gnurenga'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS=['./pelican-plugins']
PLUGINS = ['asciidoc_reader']

ASCIIDOC_CMD = 'asciidoc'

ASCIIDOC_OPTIONS = ["-a source-highlighter=pygments","-a lang=en", "-a data-uri", "-a icons"]
SUMMARY_USE_FIRST_PARAGRAPH = False

THEME = "theme"
PROFILE_IMAGE_URL = 'https://gravatar.com/sakthirengaraj'

MENUITEMS = [
    ("Blog", "tag/blog.html")
    
]

SLUGIFY_SOURCE = "basename"
CUSTOM_CSS = "static/css/custom.css"
