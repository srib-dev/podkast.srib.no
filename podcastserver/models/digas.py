# -*- coding: utf-8 -*-
"""

    digasmodels.py
    ¨¨¨¨¨¨¨¨¨
    
    READ-ONLY tabeller fra digasdatabasen.

    Disse er generert med manage.py inspectdb kommandoen :).
    ref: https://docs.djangoproject.com/en/1.11/howto/legacy-databases/

    >>> python manage.py inspectdb --database digas DEFINITION > podcastserver/digasmodels2.py
"""
from __future__ import unicode_literals

from django.db import models


class Definition(models.Model):
    """ Table for all Program names in Digas.

    Two fields are important: 
        DEFNR: the programid (int)
         NAME: the program name (string)  
    """
    defnr = models.IntegerField(db_column='DEFNR', primary_key=True)  # Field name made lowercase.
    section = models.SmallIntegerField(db_column='SECTION', blank=True, null=True)  # Field name made lowercase.
    flags = models.SmallIntegerField(db_column='FLAGS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEFINITION'


class DigasPodcast(models.Model):
    """ The Podcast Table in Digas. 

It is used by digas to store tons of info on a podcast episode.
In this app we only need a sparse subset of all the fields here, 
but to not confuse anyone, we have generated a fully mapped model.
All fields are present as they actually are in the table.

But, by using djangos queryset method `only()` we can select only 
those columns that are useful for us.

example:
podcasts = DigasPodcast.objects.using('digas').filter(
            softdel=0, 
            program=programnr).only('program', 'title', 'remark', 
                                    'author', 'createdate', 'filename', 
                                    'filesize', 'duration', 'softdel')

Don't worry about the monster code below. It's been automaticaly
created with the command: `python manage.py inspectdb --database digas PODCAST`
"""
    refnr = models.IntegerField(db_column='REFNR', primary_key=True)  # Field name made lowercase.
    class_field = models.IntegerField(db_column='CLASS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    title = models.CharField(db_column='TITLE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=254, blank=True, null=True)  # Field name made lowercase.
    filename2 = models.CharField(db_column='FILENAME2', max_length=254, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='ORIGIN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createdate = models.IntegerField(db_column='CREATEDATE', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='DURATION', blank=True, null=True)  # Field name made lowercase.
    softdel = models.SmallIntegerField(db_column='SOFTDEL', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='FLAGS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    replflags = models.SmallIntegerField(db_column='REPLFLAGS', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    personal = models.CharField(db_column='PERSONAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pool = models.CharField(db_column='POOL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    identifier = models.IntegerField(db_column='IDENTIFIER', blank=True, null=True)  # Field name made lowercase.
    registration = models.CharField(db_column='REGISTRATION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    replident = models.CharField(db_column='REPLIDENT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    musicid = models.CharField(db_column='MUSICID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gemaid = models.CharField(db_column='GEMAID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    informat = models.CharField(db_column='INFORMAT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    language = models.IntegerField(db_column='LANGUAGE', blank=True, null=True)  # Field name made lowercase.
    story = models.IntegerField(db_column='STORY', blank=True, null=True)  # Field name made lowercase.
    generation = models.SmallIntegerField(db_column='GENERATION', blank=True, null=True)  # Field name made lowercase.
    usecount = models.IntegerField(db_column='USECOUNT', blank=True, null=True)  # Field name made lowercase.
    ressort = models.SmallIntegerField(db_column='RESSORT', blank=True, null=True)  # Field name made lowercase.
    subressort = models.SmallIntegerField(db_column='SUBRESSORT', blank=True, null=True)  # Field name made lowercase.
    program = models.IntegerField(db_column='PROGRAM', blank=True, null=True)  # Field name made lowercase.
    broadcast = models.CharField(db_column='BROADCAST', max_length=40, blank=True, null=True)  # Field name made lowercase.
    broadcastdate = models.IntegerField(db_column='BROADCASTDATE', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=254, blank=True, null=True)  # Field name made lowercase.
    editor = models.CharField(db_column='EDITOR', max_length=254, blank=True, null=True)  # Field name made lowercase.
    production = models.IntegerField(db_column='PRODUCTION', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='KEYWORDS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    changeuser = models.CharField(db_column='CHANGEUSER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    changedate = models.IntegerField(db_column='CHANGEDATE', blank=True, null=True)  # Field name made lowercase.
    changetime = models.IntegerField(db_column='CHANGETIME', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.
    filesize = models.IntegerField(db_column='FILESIZE', blank=True, null=True)  # Field name made lowercase.
    audioformat = models.IntegerField(db_column='AUDIOFORMAT', blank=True, null=True)  # Field name made lowercase.
    audiomode = models.IntegerField(db_column='AUDIOMODE', blank=True, null=True)  # Field name made lowercase.
    samplerate = models.IntegerField(db_column='SAMPLERATE', blank=True, null=True)  # Field name made lowercase.
    bitrate = models.IntegerField(db_column='BITRATE', blank=True, null=True)  # Field name made lowercase.
    maxlevel = models.IntegerField(db_column='MAXLEVEL', blank=True, null=True)  # Field name made lowercase.
    sendrights = models.IntegerField(db_column='SENDRIGHTS', blank=True, null=True)  # Field name made lowercase.
    broadcastings = models.IntegerField(db_column='BROADCASTINGS', blank=True, null=True)  # Field name made lowercase.
    firstusedate = models.IntegerField(db_column='FIRSTUSEDATE', blank=True, null=True)  # Field name made lowercase.
    lastusedate = models.IntegerField(db_column='LASTUSEDATE', blank=True, null=True)  # Field name made lowercase.
    deletedate = models.IntegerField(db_column='DELETEDATE', blank=True, null=True)  # Field name made lowercase.
    recorddate = models.IntegerField(db_column='RECORDDATE', blank=True, null=True)  # Field name made lowercase.
    fadein = models.IntegerField(db_column='FADEIN', blank=True, null=True)  # Field name made lowercase.
    fadeout = models.IntegerField(db_column='FADEOUT', blank=True, null=True)  # Field name made lowercase.
    markin = models.IntegerField(db_column='MARKIN', blank=True, null=True)  # Field name made lowercase.
    markout = models.IntegerField(db_column='MARKOUT', blank=True, null=True)  # Field name made lowercase.
    intro = models.IntegerField(db_column='INTRO', blank=True, null=True)  # Field name made lowercase.
    outro = models.IntegerField(db_column='OUTRO', blank=True, null=True)  # Field name made lowercase.
    fading = models.IntegerField(db_column='FADING', blank=True, null=True)  # Field name made lowercase.
    ramp = models.SmallIntegerField(db_column='RAMP', blank=True, null=True)  # Field name made lowercase.
    donut = models.SmallIntegerField(db_column='DONUT', blank=True, null=True)  # Field name made lowercase.
    tag = models.SmallIntegerField(db_column='TAG', blank=True, null=True)  # Field name made lowercase.
    presenter = models.IntegerField(db_column='PRESENTER', blank=True, null=True)  # Field name made lowercase.
    speaker = models.IntegerField(db_column='SPEAKER', blank=True, null=True)  # Field name made lowercase.
    project = models.IntegerField(db_column='PROJECT', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    musicformat = models.IntegerField(db_column='MUSICFORMAT', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    intensity = models.IntegerField(db_column='INTENSITY', blank=True, null=True)  # Field name made lowercase.
    mood = models.IntegerField(db_column='MOOD', blank=True, null=True)  # Field name made lowercase.
    tempo = models.IntegerField(db_column='TEMPO', blank=True, null=True)  # Field name made lowercase.
    style = models.IntegerField(db_column='STYLE', blank=True, null=True)  # Field name made lowercase.
    era = models.IntegerField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    instrumentation = models.IntegerField(db_column='INSTRUMENTATION', blank=True, null=True)  # Field name made lowercase.
    target = models.IntegerField(db_column='TARGET', blank=True, null=True)  # Field name made lowercase.
    playtime = models.IntegerField(db_column='PLAYTIME', blank=True, null=True)  # Field name made lowercase.
    seasonal = models.IntegerField(db_column='SEASONAL', blank=True, null=True)  # Field name made lowercase.
    weekday = models.SmallIntegerField(db_column='WEEKDAY', blank=True, null=True)  # Field name made lowercase.
    cartpriority = models.SmallIntegerField(db_column='CARTPRIORITY', blank=True, null=True)  # Field name made lowercase.
    endcode = models.IntegerField(db_column='ENDCODE', blank=True, null=True)  # Field name made lowercase.
    carrier = models.IntegerField(db_column='CARRIER', blank=True, null=True)  # Field name made lowercase.
    motive = models.CharField(db_column='MOTIVE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    foreignmotive = models.CharField(db_column='FOREIGNMOTIVE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    spotlength = models.IntegerField(db_column='SPOTLENGTH', blank=True, null=True)  # Field name made lowercase.
    customer = models.IntegerField(db_column='CUSTOMER', blank=True, null=True)  # Field name made lowercase.
    product = models.IntegerField(db_column='PRODUCT', blank=True, null=True)  # Field name made lowercase.
    productgroup = models.IntegerField(db_column='PRODUCTGROUP', blank=True, null=True)  # Field name made lowercase.
    extdevice = models.IntegerField(db_column='EXTDEVICE', blank=True, null=True)  # Field name made lowercase.
    archivedate = models.IntegerField(db_column='ARCHIVEDATE', blank=True, null=True)  # Field name made lowercase.
    mediumtype = models.IntegerField(db_column='MEDIUMTYPE', blank=True, null=True)  # Field name made lowercase.
    mediumname = models.CharField(db_column='MEDIUMNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mediumcode = models.IntegerField(db_column='MEDIUMCODE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PODCAST'
