#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan Mulvey'
SITENAME = 'Ryan Mulvey'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# For .ipynb support, accept both .md and .ipynb as acceptable Markdown extensions
MARKUP = ('md',)

# Themes

THEME = '../pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'simplex'
#IPYNB_IGNORE_CSS=True
#IPYNB_USE_META_SUMMARY=True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
CUSTOM_CSS = 'static/css/custom.css'

# Plugins

PLUGIN_PATHS = ['./plugins/'] 
PLUGINS = ['i18n_subsites', 'ipynb.liquid']
PYGMENTS_STYLE = 'default'

#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/rem2157'),
          ('LinkedIn', 'https://www.linkedin.com/in/ryan-m-79904a14/'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = ['extra/CNAME', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/custom.css': {'path': 'static/css/custom.css'}}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
