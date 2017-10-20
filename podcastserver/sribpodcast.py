# coding: utf-8
""" See tutorial:
    https://podgen.readthedocs.io/en/latest/advanced/extending.html
"""
from lxml import etree
from podgen import Podcast

# luckily we use django, so lets validate urls from their implementation.
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class SribPodcast(Podcast):
    """This is an extension of Podcast.
    which supports abuse of link in channel to serve multi-feed-reader
    a bjørnetjeneste.

    You gain access to link by creating a new instance of this class instead
    of Podcast.
    """
    def __init__(self, *args, **kwargs):
        # Initialize the link value
        self.__link = None
        super().__init__(*args, **kwargs)

    @property
    def link(self):
        """srib.no has a multi-feed-reader plugin. It grabs the feeds from here,
        and expects a link in the channel tag that points to the feed url. they
        call it %FEEDLINK%.  google multifeedreader github  for more info.
        """
        return self.__link

    @link.setter
    def link(self, link):
        val = URLValidator()
        try:
            val(link)
        except ValidationError:
            raise ValueError("Not a valid url for link tag")
        # All checks passed
        self.__link = link

    def _create_rss(self):
        # Let Podcast generate the lxml etree (adding the standard elements)
        rss = super()._create_rss()
        # We must get the channel element, since we want to add subelements
        # to it.
        channel = rss.find("channel")
        # Only add the link element if it has been populated.
        if self.__link is not None:
            # First create our new subelement of channel.
            link = etree.SubElement(channel, 'link')
            # If we were to use another namespace, we would instead do this:
            # link = etree.SubElement(channel,
            #                        '{%s}link' % self._nsmap['prefix'])

            # Then, fill it with the link value
            link.text = str(self.__link)

        # Return the new etree, now with link
        return rss