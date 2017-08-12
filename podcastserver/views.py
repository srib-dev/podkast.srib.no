from django.shortcuts import render
from .models import Definition, DigasPodcast, ProgramInfo
from django.http import HttpResponse, JsonResponse
from podgen import Podcast, Episode, Media, Category, Person
from .util import mp3url, digas2pubdate, guid, feed_url
from .models import globalsettings 
# Create your views here.


def index(request):
    return HttpResponse('Hello World!')

def export_proginfo(request):
    from django.core import serializers
    data = serializers.serialize('json',
        ProgramInfo.objects.all())
    return HttpResponse(data, content_type="application/json")


def definitions(request):
    """ Lists all the programs from the definitino database.
 
    Should be some.
    """
    definitions = Definition.objects.using('digas').all()
    return render(request, 'definitions.htm', dict(definitions=definitions))


def allpodcasts(request):
    """ Testing how long it takes to fetch ALL podcasts with ALL fields from digas.
    """
    program="Skumma Kultur"
    definition = Definition.objects.using('digas').get(name=program)
    programnr = definition.defnr
    podcasts = DigasPodcast.objects.using('digas').filter(softdel=0, program=programnr).only('program', 'title', 'remark', 'author', 'createdate', 'broadcastdate', 'filename', 'filesize', 'duration', 'softdel')[:50]
    
    return render(request, 'podcasts.htm', dict(podcasts=podcasts, nr=len(podcasts)))



def rssfeed(request, programid):
    """ Builds the rss feed for a program identified by it's id. (int)

    1. Fetches all episodes of the program from the digas db.
    2. gets the programinfo from the app db
    3. Uses podgen to do the actual XML-generation.
    """
    podcasts = DigasPodcast.objects.using('digas').filter(
        softdel=0,
        program=int(programid)).only(
            'program', 'title', 'remark', 'author',
            'createdate', 'broadcastdate', 'filename', 'filesize',
            'duration', 'softdel').order_by('-createdate')
    programinfo = ProgramInfo.objects.get(programid=int(programid))

    p = Podcast(
        name=programinfo.name,
        subtitle=programinfo.subtitle,
        description=programinfo.description,
        website=programinfo.website,
        explicit=programinfo.explicit,
        category=Category(programinfo.category),
        authors=[globalsettings.owner],
        language=programinfo.language,
        owner=globalsettings.owner,
        feed_url=feed_url(programid),
        new_feed_url=feed_url(programid),
    )

    for episode in podcasts:
        # Get pubdate from createdate or broadcastdate
        pubdate = digas2pubdate(episode.createdate,
                                episode.broadcastdate)
        # Add the episode to the list
        p.episodes.append(
            Episode(
                title=episode.title,
                media=Media(mp3url(episode.filename), episode.filesize),
                id=guid(episode.filename),
                summary=episode.remark,
                publication_date=pubdate
            )
        )

    rss = str(p)
    return HttpResponse(rss, content_type='application/xml')
