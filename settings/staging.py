from ._base import *

BASE_URL = "http://dts.podtrac.com/redirect.mp3/podcast.srib.no"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ADMIN_ENABLED = True
INTERNAL_IPS = ['127.0.0.1']
# for debug toolbar

#ALLOWED_HOSTS = ['testcast.srib.no', 'podcast.srib.no']

# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    # Read Write for podcast programinfo
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'srib_podcast_live',
         'USER': 'srib-radio-vm',
         'PASSWORD': os.environ.get('PROGRAMINFO_DB_PASSWORD'),
         'HOST': 'db.fribyte.no',
         'PORT': '3306',
    },

     # Read only on Digas database
     'digas': {
         'ENGINE': 'django.db.backends.mysql',
         'USER': 'srib-radio-vm',
         'PASSWORD': os.environ.get('DIGAS_DB_PASSWORD'),
         'NAME': 'digas',
         'HOST': 'db.fribyte.no',
         'PORT': '3306',
     }
}

"""
        WARNING:  never set MANAGE_DIGAS_DB to True if
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
MANAGE_DIGAS_DB = False
