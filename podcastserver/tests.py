from django.test import TestCase
from django.conf import settings

from .util import feed_url

# Create your tests here.
#
# For å kjøre testene:  python manage.py test
#
# Howto write tests:
# https://docs.djangoproject.com/en/1.11/topics/testing/overview/
# ---------------------------------------------------------------


class RssFeedTest(TestCase):

    def test_feed_url(self):
        """ Sjekker om url til en podcast-rss-feed blir generert riktig.

            feed_url(id, old=False)
                kan genere urler slik de var i den gamle podcastserveren
                ved å sette old=True. By default, vil den generere
                url i nytt format, spesifisert i settings.py

        """
        programid = 8
        old_url = "http://podcast.srib.no:8080/Podcast/PodcastServlet?rss"
        old = old_url + str(programid)
        new = "%s/%s/%d" % (settings.BASE_URL, settings.FEED_PATH, programid)

        # testing new format
        url = feed_url(8)
        self.assertTrue(url == new,
                        "new feed url not built correctly. \n data: %s" % url)
        # testing old format
        url = feed_url(8, old=True)
        self.assertTrue(url == old,
                        "old feed url not built correctly. \n data: %s" % url)
