# podkast.srib.no
Podcast publication server for Studentradioen i Bergen



## Hvordan systemet er skrudd sammen

Podkastjeneren bruker python. Det består av webrammeverket Django og et podkast rss bibliotek (podgen) som Radio Revolt har laget.

## Setup:
Disse stegene utføres for å sette opp et lokalt utviklingsmiljø for podkastserveren. I.e det du må gjøre for å få ting opp og kjørende, lokalt.

Før du kjører listen her bør du ha på plass **Python, Pip og Virtualenvwrapper**. 

Hvordan ha de på plass? sjekk her: [Sette opp Python](./docs/Sette-opp-Python.md)



1. ```git clone https://github.com/srib-dev/podkast.srib.no```
2. lag virtualenv: ```mkvirtualenv podkast```
3. Installer dependencies: ```pip install -r requirements_dev.txt```
4. lag ny fil `settings.py` i mappen `podkast` med følgende innhold:

```python
# -*- coding: utf-8 -*-

from .base_settings import *
# Gjør kun dette lokalt på egen pc. 
# Når vi jobber med en lokal juksedatabase.
# Aldri på den ekte digas databasen...
MANAGE_DIGAS_DB = True

# Django admin side flyttet til: http://localhost:8000/djangoadmin
# (vi har hijacket /admin til eget bruk.)
ADMIN_ENABLED = True

# Nyttig når vi utvikler lokalt. Ikke på den ekte servern.
DEBUG = True

```
5. Kjør ```python installer.py```


# Start serveren (lokalt)
For å kunne komme inn på podkastsidene lokalt bruker vi djangos innebygde httpserver. Da kjører den på din maskin, og vil kun være synlig og tilgjengelig for deg.

1. ```python manage.py runserver```
2. Gå til http://localhost:8000 i nettleseren. ;D"


# Kjøre serveren i produksjon:

For å kjøre i produksjon må du koble deg opp mot to mysql databaser. En for podcast programmet og en tilkobling til Digas databasen.

Man må og koble seg opp mot NAS'et hvor alle mediafilene ligger lagret. Dette gjøres typisk i Ubuntu med kommandoen `sudo mount -vvv -w -t nfs xxx.xx.x.xxx:/NAS /home/fribyte/srib-nas-mount/NAS`. Da blir alle filene på NAS-en tilgjengelig i ubuntu filsystemet. Deretter må man gjøre denne mappen tilgjengelig for docker containeren ved en mount som dette: `docker run --name srib-podcast -d --restart=always -p 80:80 --mount type=bind,source=/home/fribyte/srib-nas-mount/NAS/digasLydfiler/podcast,target=/media/podcast,readonly srib-podcast`.

Eksempel på `podkast/settings.py` for prod:

```
from .base_settings import *

BASE_URL = "http://dts.podtrac.com/redirect.mp3/podcast.srib.no"
STATIC_ROOT = '/var/www/podcast.srib.no/www/static'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'En-eller-annen-secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ADMIN_ENABLED = True
INTERNAL_IPS = ['127.0.0.1']
# for debug toolbar

#ALLOWED_HOSTS = ['staging.podcast.srib.no', 'podcast.srib.no']


# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    # Read Write for podcast programinfo
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'srib_podcast_live',
         'USER': 'srib-radio-vm',
         'PASSWORD': 'super-duper-passord',
         'HOST': 'db.fribyte.uib.no',
         'PORT': '3306',
    },

     # Read only on Digas database
     'digas': {
         'ENGINE': 'django.db.backends.mysql',
         'USER': 'srib-radio-vm',
         'PASSWORD': 'super-duper-passord',
         'NAME': 'digas',
         'HOST': 'db.fribyte.uib.no',
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
```