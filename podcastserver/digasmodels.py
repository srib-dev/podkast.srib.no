# -*- coding: utf-8 -*-
"""

    digas.py - Digas Models
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

    READ-ONLY tabeller fra digasdatabasen.

    Disse er generert med manage.py inspectdb kommandoen :).
    ref: https://docs.djangoproject.com/en/1.11/howto/legacy-databases/

    >>> python manage.py inspectdb --database digas DEFINITION > podcastserver/digasmodels2.py
"""
from __future__ import unicode_literals

from django.db import models


class Definition(models.Model):
    defnr = models.IntegerField(db_column='DEFNR', primary_key=True)  # Field name made lowercase.
    section = models.SmallIntegerField(db_column='SECTION', blank=True, null=True)  # Field name made lowercase.
    flags = models.SmallIntegerField(db_column='FLAGS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEFINITION'
