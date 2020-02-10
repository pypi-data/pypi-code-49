# -*- coding: utf-8 -*-
"""
Base settings for Py Html Checker pages
"""
import os
from webassets import Bundle

from .jinja_filters import highlight_html_filter
# Register custom webasset filter for RCssMin minifier
from webassets.filter import register_filter
from .webassets_filters import RCSSMin
register_filter(RCSSMin)

DEBUG = True

PROJECT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
    )
)

# Common site name and domain to use available in templates
SITE_NAME = 'Py Html Checker'
SITE_DOMAIN = 'localhost:8001'

# Sources directory where the assets will be searched
SOURCES_DIR = os.path.join(PROJECT_DIR, 'sources')
# Templates directory
TEMPLATES_DIR = os.path.join(SOURCES_DIR, 'templates')
# Directory where all stuff will be builded
PUBLISH_DIR = os.path.join(PROJECT_DIR, '_build/dev')
# Path where will be moved all the static files, usually this is a directory in
# the ``PUBLISH_DIR``
STATIC_DIR = os.path.join(PROJECT_DIR, PUBLISH_DIR, 'static')
# Path to the i18n messages catalog directory
LOCALES_DIR = os.path.join(PROJECT_DIR, 'locale')

# Locale name for default language to use for Pages
LANGUAGE_CODE = "en"

# Additional template filters
JINJA_FILTERS = {
    "highlight_html": highlight_html_filter,
}

# A list of locale name for all available languages to manage with PO files
LANGUAGES = (LANGUAGE_CODE,)

# The static url to use in templates and with webassets
# This can be a full URL like http://, a relative path or an absolute path
STATIC_URL = 'static/'

# Extra or custom bundles
BUNDLES = {
    'main_css': Bundle(
        'css/main.css',
        filters='rcssmin',
        output='css/main.min.css'
    ),
    'styleguide_css': Bundle(
        'css/styleguide_page.css',
        filters='rcssmin',
        output='css/styleguide_page.min.css'
    ),
}

# Sources files or directory to synchronize within the static directory
FILES_TO_SYNC = (
    #'images',
    #'fonts',
    'css',
)
