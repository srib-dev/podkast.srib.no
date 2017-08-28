# podkast.srib.no
Podcast publication server for Studentradioen i Bergen



## Hvordan systemet er skrudd sammen

Podkastjeneren bruker python. Det består av webrammeverket Django  og et podkast rss bibliotek som Radio Revolt har laget, (podgen).

## Setup:
Disse stegene utføres for å sette opp et lokalt utviklignsmiljø for podkastserveren. I.e det du må gjøre for å få ting opp og kjørende, lokalt.

(Ikke kjør setupscriptet i produksjon!)


1. ```git clone https://github.com/srib-dev/podkast.srib.no```
2. lag virtualenv: ```mkvirtualenv podkast```
3. Installer dependencies: ```pip install -r requirements_dev.txt```
4. lag ny fil `settings.py` i podkast mappen med følgende innhold:
    ```python
    from .base_settings import *
    # Gjør kun dette lokalt på egen pc. 
    # Når vi jobber med en lokal juksedatabase.
	# Aldri på den ekte digas databasen...
    MANAGE_DIGAS_DB = True

    # Nifty local admin interface for devs only.
    # Accesible at [http://localhost:8000/djangoadmin](http://localhost:8000/djangoadmin)
    # (vi har hijacket /admin til eget bruk.)
    ADMIN_ENABLED = True

    # Nyttig når vi utvikler lokalt. Ikke på den ekte servern (farlig).
	DEBUG = True

    ```
5. Kjør ```./setup_dev_environment.sh```

6. Last inn tulledata ved hjelp av django sitt manage.py skript:
	```python manage.py loaddata tull```



## Hello World Django

Om django er nytt for deg kjør gjennom en tutorial herifra fra start til slutt - så lærer du fort og i en fei!
[Start med Django](https://www.djangoproject.com/start/)
