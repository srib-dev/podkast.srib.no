from django.shortcuts import render
from .models import Definition, DigasPodcast, ProgramInfo
from django.http import HttpResponse, JsonResponse
from podgen import Podcast, Episode, Media, Category, Person
import pytz
import datetime
# Create your views here.


def helenesofies(request, antall):
    return HttpResponse("Helene " * int(antall) )


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
    podcasts = DigasPodcast.objects.using('digas').filter(softdel=0, 
        program=programid).only('program', 'title', 'remark', 'author', 
            'createdate', 'broadcastdate', 'filename', 'filesize', 'duration', 'softdel')
    programinfo = ProgramInfo.objects.get(programid=int(programid))

    TIME_ZONE = pytz.timezone('Europe/Oslo')
    owner = Person("Studentradion i Bergen", "kontakt@srib.no")

    p = Podcast(
        name=programinfo.name,
        subtitle=programinfo.subtitle,
        description=programinfo.description,
        website=programinfo.website,
        explicit=programinfo.explicit,
        category=Category(programinfo.category),
        authors=[Person("Skumma Kultur", "ansvarlig.redaktor@srib.no")],
        language=programinfo.language,
        owner=owner)

    p.episodes += [
    Episode(
        title="BDSM",
        media=Media(
            "http://srib.no/bdsm.mp3", 19238194),
        summary="Hvordan bruke bdsm i studio",
        publication_date=datetime.datetime(
            2017, 7, 21, 17, 18, tzinfo=TIME_ZONE)
    ),
    Episode(
        title="Ensomhet i kunsten",
        media=Media(
            "http://srib.no/ensomhet.mp3", 1734734774),
        summary="Hva er ensomhet? I studio var Samantha Hatten og han med Barten. Med gjest Daniel Katten"),
    Episode(
        title="Studentene kjeder seg",
        media=Media(
            "http://srib.no/kjedsomhet.mp3", 1734734774),
        summary="Hvorfor kjeder studentene seg?  - med gjest Gaute Grøtta Grav")
    ]


    rss = str(p)
    return HttpResponse(rss, content_type='application/xml')
