# -*- coding: utf-8 -*-

"""
Django settings for podkast project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
from podgen import Person

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h)a11b^x61y)(sqzsootokuqf@ip25vw-v+*9=pypm9r+$9ee='



###################################################
#
#   RSS Feed settings
#
###################################################

BASE_URL = "http://127.0.0.1:8000"
""" Base of the url(s) to rss feeds.

    The domain and possible port to the podcast server.
"""

OLD_BASE_URL = "http://podcast.srib.no:8080"
""" The base url on the old java server we used between 2009-2017

    This is used to tell itunes we moved. We need to have redirects
    set up so all traffic coming in to this old url is routed to the
    new feed and episode links. This should be handled in the
    webserver, and preferably by Fribyte. 
"""

OLD_FEED_URL_FORMAT = "http://podcast.srib.no:8080/Podcast/PodcastServlet?rss%d"
""" old RSS feed url format.

    to use this do this:
        programid = 9
        old_feed_url = OLD_FEED_URL_FORMAT % (programid,)
"""

GUID_URL = "http://podcast.srib.no:8080/podcast"
""" Part of the Global Unique ID of podcast episodes.

    "It is important that an episode keeps the same ID until the end of time,
    since the ID is used by clients to identify which episodes have been
    listened to, which episodes are new, and so on. Changing the ID causes
    the same consequences as deleting the existing episode and adding a new,
    identical episode."
        https://podgen.readthedocs.io/en/latest/api.episode.html#podgen.Episode.id

    Therefore we MUST set the global id of the episode to the same format
    as was used between 2009-2017 on the old podcast server.
    It was:
        http://podcast.srib.no:8080/podcast/<filename>.mp3

    Please note:
        -no https.

"""

FEED_PATH = "feed"
""" Part of the url(s) to rss feeds.

    Use no trailing slash or prepending slash.

    With a BASE_URL of https://podkast.srib.no and a FEED_PATH of "feed"
    a rss feed with id 8 (Skumma kultur) would have the url to it's RSS feed
    looking like this:
        https://podkast.srib.no/feed/8
"""

SOUNDFILE_PATH = "podcast"
""" Part of the url that are used for the sound files

    This is used to build the urls for the actual mp3 files.
    example:

    With a BASE_URL of https://podkast.srib.no and SOUNDFILE_PATH of "podcast"
    the resulting url looks like this:
        https://podkast.srib.no/podcast/SRRED102_ACADE23123BACADFE.mp3
"""



#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}
#CONSTANCE_DATABASE_CACHE_BACKEND = 'default'


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'constance',  # for having settings in admin interface
    'constance.backends.database',  # same as above
    'podcastserver',
]

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'THE_ANSWER': (42, 'Answer to the Ultimate Question of Life, '
                       'The Universe, and Everything'),

    'OWNER_NAME': ('Studentradioen i Bergen',
                   'Navn på eieren til podcastene.'
                   'Bør være Studentradioen i Bergen.'),

    'OWNER_EMAIL': ('kontakt@srib.no',
                    'Epost til eier av podcastene.'
                    'Pleier å være kontakt@srib.no'),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'podkast.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['podcastserver/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#WSGI_APPLICATION = 'podkast.wsgi.application'


# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'digas': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'digasdb.sqlite3'),
    }
}
#########################################################
#
#   For Testing purposes, use a temporary memory based
#   database. Forgetting those real db-s from up above.
#
#########################################################
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        },
        'digas': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    }


"""
        WARNING:  never set MANAGE_DIGAS_SCHEMA to True if 
                  the `digas` database is set to the real
                  mysql digas database. It can potentially
                  delete the tables!

        What this does is that it will let django manage the 
        life cycle of the tables belonging to the models
        for podcasts and definitions in the digasmodels file.

        These models maps the Digas DB tables PODCAST and DEFINITION.
        Real data, straight from digas. So we don't want django to 
        delete and create these tables if we run `python manage.py migrate`.

        It's only safe to set this to true if you use a fake digas database (
        i.e a localhost mysql server for development or a sqlite file).
"""
MANAGE_DIGAS_SCHEMA = False


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'nb'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

ALLOWED_HOSTS = ['staging.podcast.srib.no', 'podcast.srib.no']