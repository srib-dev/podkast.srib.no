# -*- coding: utf-8 -*-

"""
	admin.py: registrerer hvilke modeller som 
		  skal være synlig i django admin.

"""

from django.contrib import admin
from .models import Person, ProgramInfo, Definition, DigasPodcast
from django.conf import settings


# Register your models here.
# admin.site.register(Person)
admin.site.register(ProgramInfo)

if settings.MANAGE_DIGAS_DB == True:
	# Legger til digastabellene om vi får 
	# tukle med dem. Altså, da bør de være en lokal kopi, 
	#  -- ikke tukle med Ekte Digas!!
	admin.site.register(Definition)
	admin.site.register(DigasPodcast)
