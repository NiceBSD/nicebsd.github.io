#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NiceBSD'
SITENAME = u'NiceBSD'
SITEURL = ''

TIMEZONE = 'America/Edmonton'

PATH = 'content/'
OUTPUT_PATH = '../'
DEFAULT_LANG = u'en'
TYPOGRIFY = True
DIRECT_TEMPLATES = ('index', 'archives')

AUTHOR_SAVE_AS = False
TAG_SAVE_AS = False
CATEGORY_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('OpenBSD', 'http://openbsd.org/'),
          ('NetBSD', 'https://netbsd.org/'),
          ('FreeBSD', 'https://freebsd.org/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
