# -*- coding: utf-8 -*-
"""  This script is to setup the local development environment
  Assumption:  settings is configured to use sqlite database
                for the digas database!

   Do not run this thingy in production.
"""
import os
import sys
import subprocess
import django

# Forteller hvor django finner settingsene for podkastprosjektet.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "podkast.settings")
django.setup()


#  Most work done here to the default database.
subprocess.call("python manage.py migrate", shell=True)

#  Secondly, we create tables for the local fake dev digas sqlite db. 
#  
#  Will produce an error "missing django_content_types" or something
#  -- ignore it, those are already installed in the default db.
subprocess.call("python manage.py migrate --database digas podcastserver 0001", shell=True)

print( "\n" * 4)
print(""" 
	Ignore the error above if it says:
	django.db.utils.OperationalError: no such table: django_content_type


	Lets create a superuser now.
	""")

#createsuperuser (googled how to automate creating superuser django)
from django.contrib.auth.models import User 
User.objects.create_superuser('admin', 'admin@example.com', '1234')

print("""
    -------------------------------------------------------------------
    ALMOST DONE 
    ------------------------------------------------------------------- 
  	Superuser Admin created: 
	  	username: admin
	  	password: 1234

  	OK :). Take note. 


    And now you should load test data into the local databases.
	""")


def load_tulledata():
	print("Laster mockdata inn i db. For å ha noe der. Podcasts og sann.")
	subprocess.call('python manage.py loaddata --database digas digastull', shell=True)
	subprocess.call('python manage.py loaddata --database default podcasttull', shell=True)


# Hack to make py2 and py3 input work.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
if sys.version[0] =='2':
	input = raw_input

load_it = input("Vill du laste inn testdata til bruk for utvikling? (ja/nei): ")
if 'j' in load_it.lower():
	load_tulledata()

def the_end():
	return """
	FINISHED SETTING UP LOCAL DEVELOPMENT ENVIRONMENT :)!

	Hint: you might want to do this now:
	  1. run: python manage.py runserver
	  2. go to http://127.0.0.1:8000 in your browser.
	"""

print(the_end())