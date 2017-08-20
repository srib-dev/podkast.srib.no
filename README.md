# podkast.srib.no
Podcast publication server for Studentradioen i Bergen



## Hvordan systemet er skrudd sammen

Podkastjeneren bruker python. Det består av webrammeverket Django  og et podkast rss bibliotek som Radio Revolt har laget, (podgen).

## Setup:
Disse stegene utføres for å sette opp et lokalt utviklignsmiljø for podkastserveren. I.e det du må gjøre for å få ting opp og kjørende, lokalt.

(Ikke kjør setupscriptet i produksjon!)


1. ```git clone ...```
2. lag virtualenv: ```mkvirtualenv podkast```
3. Installer dependencies: ```pip install -r requirements_dev.txt```
4. lag ny fil `settings.py` i podkast mappen med følgende innhold:
    ```
    from .base_settings import *
    # Gjør kun dette lokalt på egen pc.
    MANAGE_DIGAS_SCHEMA = True
    ```
5. Få tak i  fixture filene fra Robin, legg dem i podcastserver/fixtures/
4. Kjør ```./setup_dev_environment.sh```


## Hello World Django

Om django er nytt for deg kjør gjennom en tutorial herifra fra start til slutt - så lærer du fort og i en fei!
[Start med Django](https://www.djangoproject.com/start/)