from django.shortcuts import render, redirect
from .models import Definition, DigasPodcast, ProgramInfo
from django.http import HttpResponse, JsonResponse
from podgen import Podcast, Episode, Media, Category, Person
from .util import mp3url, digas2pubdate, guid, feed_url
from django.conf import settings
from django.utils import timezone


def srib_admin(request):
    # Henter ut alle podcastprogrammer

    if request.user.is_authenticated:
        programs = ProgramInfo.objects.all()
        return render(request, 'admin.htm', dict(programs=programs))
    else:
        return render(request, 'registration/login.html')


def teknisksjef(request):
    i = request.GET["i"]
    return render(request, 'sjef.htm', dict(i=i))


def index(request):
    # Henter ut kun programmer som har publish satt til True.
    publiserte_programmer = ProgramInfo.objects.filter(publish=True)
    return render(request, 'index.htm', dict(programs=publiserte_programmer))


def definitions(request):
    """ Lists all the programs from the definitino database.
    Should be some.
    """
    definitions = Definition.objects.using('digas').all()
    return render(request, 'definitions.htm', dict(definitions=definitions))


def thumbnail(request, programid):
    """ returns a redirect to the url for the podcast image """
    program = ProgramInfo.objects.get(programid=int(programid))
    return redirect(program.image_url)


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

    # loading globalsettings here, and not at the module_level
    # This way django won't explode because of missing
    # constance_config table when we start on scratch
    # or set up in a new environment.
    from .models import globalsettings

    p = Podcast(
        name=programinfo.name,
        subtitle=programinfo.subtitle,
        description=programinfo.description,
        website=feed_url(programid),  # programinfo.website,
        explicit=programinfo.explicit,
        category=Category(programinfo.category),
        authors=[globalsettings.owner],
        language=programinfo.language,
        owner=globalsettings.owner,
        feed_url=feed_url(programid),
        new_feed_url=feed_url(programid),
        image=programinfo.image_url,
    )

    for episode in podcasts:
        # Get pubdate from createdate or broadcastdate
        pubdate = digas2pubdate(episode.createdate,
                                episode.broadcastdate)

        if pubdate > timezone.now():
            continue

        # Add the episode to the list
        p.episodes.append(
            Episode(
                title=episode.title,
                media=Media(mp3url(episode.filename), episode.filesize),
                link=mp3url(episode.filename),  # multifeedreader uses this.
                id=guid(episode.filename),
                summary=episode.remark,
                publication_date=pubdate
            )
        )

    # send it as unicode
    rss = u'%s' % p
    return HttpResponse(rss, content_type='application/xml')
