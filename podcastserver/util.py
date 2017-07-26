# -*- coding: utf-8 -*-
"""

    utils.py
    ¨¨¨¨¨¨¨¨¨

    Collection of usefull utitilities for the podcast server.
"""
import os.path
from django.conf import settings
import pytz
from datetime import datetime
from django.urls import reverse

def feed_url(programid, old=False):
    """ returns full url to a feed given its programid (int).

        If old is set to True, it will return the old url format.

        see doc: https://docs.djangoproject.com/en/1.11/ref/urlresolvers/#reverse
    """
    if old == True:
        # For backwards compatibility.
        return settings.OLD_FEED_URL_FORMAT % programid
    else:
        # Returns the new format. Using the current urlformat 
        # from settings.
        path = reverse('rssfeed', 
                        args=(programid,))
        return settings.BASE_URL + path


def mp3url(filepath):
    r""" Take in a filepath to an MP3 file and return it's url.

        In the digas database the filepaths can have different value.
        The most common is:
        W:\<filename.mp3>

        W: is the network mounted folder Podcasts that resides in the NAS.

        But it could also have the value:

        \\srarkiv2\<filename.mp3>

        In the old days, we put stuff in these servers, they seem not used
        anymore. So accessing the file will actually not work unless we
        hook the servers up again.

        All new episodes and the most recent active, functioning podcast
        episodes will be using the W:\<filename> format. We therefore need
        to test a given filename if it really works, and to map a url to
        the filename.

        The problem to solve is:
            Given an Filename to an podcast episode (mp3)
            - verify that the soundfile is accesible and work.
            - map different filepaths to the url. And the reverse:
            - map a episode url to a given filepath.
    """
    filepath = filepath.replace("w:\\", "")
    filepath = filepath.replace("W:\\", "")
    return "%s/%s/%s" % (settings.BASE_URL, settings.SOUNDFILE_PATH, filepath)


def guid(filepath):
    """ return Global Unique ID of podcast episode from filename.

    "It is important that an episode keeps the same ID until the end of time,
    since the ID is used by clients to identify which episodes have been
    listened to, which episodes are new, and so on. Changing the ID causes
    the same consequences as deleting the existing episode and adding a new,
    identical episode."
        https://podgen.readthedocs.io/en/latest/api.episode.html#podgen.Episode.id

    Therefore we MUST set the global id of the episode to the same format
    as was used between 2009-2017 on the old podcast server. At least for 
    those episodes. At the time of writing, I'm running out of dev-time
    so I choose the guid to always be the same format, even for new episodes.

    It was (and now also is):
        http://podcast.srib.no:8080/podcast/<filename>.mp3

    Please note:
        -no https.

    """
    filepath = filepath.replace("w:\\", "")
    filepath = filepath.replace("W:\\", "")
    return "%s/%s" % (settings.GUID_URL, filepath)


def digas2pubdate(createdate, broadcastdate=0):
    """ Convert dates found in the digas db and selects a pubDate.

        Check if there is a Broadcastdate set, 
        otherwise pick createdate as the publication date.

        Also, make the date timezone aware. Which is a bit silly.
        Since it is only a date. 
    """
    digasformat = "%Y%m%d" #yyyymmdd
    createdate = datetime.strptime(str(createdate), digasformat)
    try:
        # Some broadcastdates are blank in digas, they are stored as "0"
        # in the DB.
        broadcastdate = datetime.strptime(str(broadcastdate), digasformat)
        pubdate = broadcastdate
    except:
        pubdate=createdate

    # Make it timezone aware
    tz = pytz.timezone(settings.TIME_ZONE)
    pubdate = pubdate.replace(tzinfo=tz)
    return pubdate


