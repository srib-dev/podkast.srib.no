# -*- coding: utf-8 -*-
"""

    globalsettings.py
    ¨¨¨¨¨¨¨¨¨

    Global Settings for the server that will be stored in the db
    and can be edited through the website by staff/nettredaktor.

    Using the django-dbsettings module:
    docs: https://github.com/zlorf/django-dbsettings

"""
import dbsettings


class GlobalOwner(dbsettings.Group):
    """ Global eier til podcastene.

    Brukes for å si til iTunes at vi eier dem."""

    name = dbsettings.StringValue(
        'Navn på eieren til podcastene. Bør være Studentradioen i Bergen.',
        default='Studentradioen i Bergen'
    )
    email = dbsettings.StringValue(
        'Epost til eier. pleier være kontakt@srib.no',
        default='kontakt@srib.no')


owner = GlobalOwner()