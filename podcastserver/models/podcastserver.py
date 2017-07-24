# -*- coding: utf-8 -*-
"""

    models.py
    ¨¨¨¨¨¨¨¨¨
    
    Modeller for databasen i podkastserveren.
"""
from django.db import models
from django.conf.global_settings import LANGUAGES
from podgen.category import Category


CATEGORIES = ((c,c) for c in Category._categories.keys())
""" Getting iTunes Store supported categories from the podgen module.
    
    See list here: https://github.com/tobinus/python-podgen/blob/master/podgen/category.py#L39-L67

    Django needs choices in the following tuple format:
    ( 
        ('Choice1': "Choice one human readable"),
        ('Choice1': "Choice one human readable")
    )

"""

class Person(models.Model):
    u"""
        Person = <Name, Email>
    """
    fullname = models.CharField(max_length=128)
    email = models.EmailField(max_length=70,blank=True)


class ProgramInfo(models.Model):
    u"""Description: The info on a podcast.

    Denne klassen brukes for å administrere selve
    podcasten. Episodene har egne datafelt, som man
    finner i Episode-klassen.
    """
    programid = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    description = models.TextField()
    website = models.URLField(null=True, max_length=100)
    explicit = models.BooleanField()
    publish = models.BooleanField(default=False)
    authors = models.ManyToManyField(Person, related_name='authors',
                                     blank=True)
    language = models.CharField(max_length=7, choices=LANGUAGES, default='nb')
    """ Language of the podcast.

    Codes supported seems to be 21.
    For a list see here:
    http://www.ibabbleon.com/iOS-Language-Codes-ISO-639.html
    """

    category = models.CharField(max_length=20, choices=CATEGORIES)
    """ iTunes Category of the podcast. 

    This choices list can be used by Django Forms to provide the user
    their --- choices when selecting a category. So we like to provide
    them with only valid iTunes Categories.
    """

    image_url = models.URLField(null=True, max_length=500)
    """ Details about image specs below.

    from the podgen documentation:

        The URL of the artwork for this podcast. iTunes prefers square images 
        that are at least 1400x1400 pixels.
        Podcasts with an image smaller than this are not eligible to be 
        featured on the iTunes Store.

        iTunes supports images in JPEG and PNG formats with an RGB color space 
        (CMYK is not supported). The URL must end in ”.jpg” or ”.png”; if they 
        don’t, a NotSupportedByItunesWarning will be issued.

        http://podgen.readthedocs.io/en/latest/user/basic_usage_guide/part_1.html#image
    """

    owner = models.ForeignKey(Person)
    """<itunes:owner>  - the legal owner of the podcast.

    should be: Studentradioen i Bergen - kontakt@srib.no
    """

    def __str__(self):
        """ Denne magiske funksjonen sier hvordan print(podcast) vil se ut.

        Eksempel:
            <Podcast Skumma Kultur>
        """
        return "<Podcast %s>" % self.title
