# This script is to setup the local development environment
# Assumption:  settings is configured to use sqlite database
#               for the digas database!
#
#  Do not run this thingy in production.
#
#  Windows: copy this file, remove comments, and save it as a .bat
#           probably works to run it.
#
#################################################################

# Most work done here to the default database.
python manage.py migrate

# Secondly, we create tables for the local fake dev digas sqlite db. 
# 
# Will produce an error "missing django_content_types" or something
# -- ignore it, those are already installed in the default db.
python manage.py migrate --database digas podcastserver 0001

echo 
echo 
echo 
echo 
echo " Ignore the error above if it says:"
echo " django.db.utils.OperationalError: no such table: django_content_type"
echo 
echo 
echo 
echo
echo " Lets create a superuser now."
echo "Type in the admin account name below "
echo 
echo 
echo 
python manage.py createsuperuser
echo 
echo " OK :). - And now we will load data into the local databases."
echo
echo
################################################
#   LOADING DATA FROM FIXTURES
#
#   If this fails, make sure you have the fixtures
#   files in the fixtures folder. 
#   
#   (basically json files with data, one for each table)
# 
################################################

# Loading fixtures with data from DIGAS 

echo "Definition = List of programnames and their programid(int)"
python manage.py loaddata --database digas definition

echo  "Podcast = the big thing with all the data about the podcasts in digas."
python manage.py loaddata --database digas podcast


################################################
#       Programinfo
#
# second up, the podcastserver hosted data about the
# podcast programs. So called - programinfo.
#   AND authors (persons)
################################################
echo "Person - authors of podcasts"
python manage.py loaddata --database default person

echo "Programinfo - details about a podcast program"
python manage.py loaddata --database default programinfo

echo
echo    "       FINISHED SETTING UP LOCAL DEVELOPMENT ENVIRONMENT :)!"
echo
echo "Hint: you might want to do this now:"
echo "  1. run: python manage.py runserver"
echo "  2. go to http://127.0.0.1:8000 in your browser."
