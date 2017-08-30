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
echo " Type in the admin account name below "
echo 
echo 
echo 
python manage.py createsuperuser
echo
echo    -------------------------------------------------------------------
echo    ALMOST DONE 
echo    ------------------------------------------------------------------- 
echo
echo
echo " OK :). - And now you should load data into the local databases."
echo
echo "             ./load_tulle_data.sh"
echo
echo
echo
echo
