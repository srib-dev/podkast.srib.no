# -*- coding: utf-8 -*-
"""

    globalsettings.py
    ¨¨¨¨¨¨¨¨¨

    Global Settings for the server that will be stored in the db
    and can be edited through the website by staff/nettredaktor.

    Using the django-constance module to store config in db. 
    Config can then be edited in the admin interface. 

    https://django-constance.readthedocs.io/en/latest/
"""

# from constance import config
from podgen import Person

owner = Person(name='Studentradioen i Bergen',
               email='kontakt@srib.no')
""" Standard eier til podcastene.

Blir sendt til itunes via rss feeden.
for å forandre eier gå til /admin i browseren under
CONSTANCE.

For å legge til flere globale config-variabler gå til
settings.py og titt på CONSTANCE_CONFIG.
"""
