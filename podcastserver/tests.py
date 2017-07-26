from django.test import TestCase
from django.conf import settings

from .util import feed_url

# Create your tests here.
class RssFeedTest(TestCase):

    def test_feed_url(self):
        programid = 8
        old = "http://podcast.srib.no:8080/Podcast/PodcastServlet?rss" + str(programid) 
        new = "%s/%s/%d" % (settings.BASE_URL, settings.FEED_PATH, programid)

        url = feed_url(8)
        self.assertTrue(url == new, "new feed url not built correctly. \n data: %s" % url)
        url = feed_url(8, old=True)
        self.assertTrue(url == old, "old feed url not built correctly. \n data: %s" % url)
