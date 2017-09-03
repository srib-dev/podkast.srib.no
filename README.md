# podkast.srib.no
Podcast publication server for Studentradioen i Bergen



## Hvordan systemet er skrudd sammen

Podkastjeneren bruker python. Det består av webrammeverket Django  og et podkast rss bibliotek som Radio Revolt har laget, (podgen).

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


## Hello World Django

Om django er nytt for deg kjør gjennom en tutorial herifra fra start til slutt - så lærer du fort og i en fei!
[Start med Django](https://www.djangoproject.com/start/)
