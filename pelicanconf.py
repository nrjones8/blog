#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nick Jones'
SITENAME = u'Nick Jones'
SITEURL = ''

TIMEZONE = ''

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# The social sidebars are kinda noisy, just remove them
SOCIAL = None

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ["images", ]

# http://docs.getpelican.com/en/stable/settings.html#url-settings
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DEFAULT_DATE_FORMAT = '%B %d, %Y'


THEME = 'themes/tuxlite_tbs'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
