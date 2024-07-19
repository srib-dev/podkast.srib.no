# -*- coding: utf-8 -*-

from ._base import *
# Gjør kun dette lokalt på egen pc. 
# Når vi jobber med en lokal juksedatabase.
# Aldri på den ekte digas databasen...
MANAGE_DIGAS_DB = True

# Django admin side flyttet til: http://localhost:8000/djangoadmin
# (vi har hijacket /admin til eget bruk.)
ADMIN_ENABLED = True

# Nyttig når vi utvikler lokalt. Ikke på den ekte servern.
DEBUG = True