# This is meant to load a dump of production data in fixtures 
# to be used on a local dev environment.

# -- not for production --


################################################
#   LOADING DATA FROM FIXTURES
#
#   If this fails, make sure you have the fixture
#   files in the fixtures folder. 
#   
#   (basically json files with data, one for each table)
# 
################################################

# Loading fixtures with data from DIGAS 
echo " Loading Digas tulledata.  "
echo " To databasetabeller:"
echo "      Definition = List of programnames and their programid(int)"
echo "      Podcast = the big thing with all the data about "
echo "                                the podcasts in digas."
python manage.py loaddata --database digas digastull



################################################
#       Programinfo
#
# second up, the podcastserver hosted data about the
# podcast programs. So called - programinfo.
#   AND authors (persons)
################################################
echo " Loading Podcastserver tulledata. "
echo " To databasetabeller:"
echo "      Person - authors of podcasts"
echo "      Programinfo - details about a podcast program"
python manage.py loaddata --database default podcasttull


echo
echo    "       FINISHED SETTING UP LOCAL DEVELOPMENT ENVIRONMENT :)!"
echo
echo "Hint: you might want to do this now:"
echo "  1. run: python manage.py runserver"
echo "  2. go to http://127.0.0.1:8000 in your browser."
