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
MARKUP = ('md', 'ipynb')

# Themes

THEME = '../pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'darkly'

#
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Plugins

PLUGIN_PATHS = ['./plugins/'] 
#PLUGINS = ['i18n_subsites', 'ipynb.markup', 'liquid_tags.notebook']
PLUGINS = ['i18n_subsites', 'liquid_tags.notebook']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/rem2157'),
          ('LinkedIn', 'https://www.linkedin.com/in/ryan-m-79904a14/'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
