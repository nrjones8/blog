#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nick Jones'
SITENAME = u'Nick Jones'
SITEURL = ''
# i am not creative
SITETITLE = 'Nick Jones'
# really, really not creative
SITESUBTITLE = ''
SITEDESCRIPTION = "Nick Jones's personal website and blog"
#FAVICON = SITEURL + '/images/favicon.ico'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


SOCIAL = (
    ('github', 'https://github.com/nrjones8'),
    ('twitter', 'https://twitter.com/nrjones8')
)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ["images", "static"]
EXTRA_PATH_METADATA = {
    # thanks https://stackoverflow.com/a/44209338
    'static/google71a1aae577e78d5a.html': {'path': 'google71a1aae577e78d5a.html'}
}

JINJA_ENVIRONMENT = {}
THEME_STATIC_DIR = 'static'
DISABLE_URL_HASH = True

# http://docs.getpelican.com/en/stable/settings.html#url-settings
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DEFAULT_DATE_FORMAT = '%B %d, %Y'


THEME = 'themes/Flex'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
