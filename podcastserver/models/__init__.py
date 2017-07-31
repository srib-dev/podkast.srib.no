# coding: utf-8
""" Package level file that makes all our models accesible.

To make django see all our models we import them. They are in two
main files (digas.py and podcastserver.py) in the models folder.

If you add more models, make sure they are imported here.
That way manage.py makemigrations and manage.py migrate will
work with them.
"""
# Digas models
from .digasmodels import Definition, DigasPodcast
# podcastserver app models
from .podcastmodels import Person, ProgramInfo
