"""podkast URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

# Step 1. Import the view functions
from podcastserver.views import *

# Step 2. Route urls to the view function
urlpatterns = [
    url(r'^defs', definitions),
    url(r'^bloat', allpodcasts),
    url(r'^feed/(\d+)', rssfeed),
]


# This is just magic for having a development and deployment
# version of the application to be run by the same code base.
# In production we don't wan't the django default admin interface
# nor the debug toolbar.
# Both these can therefore be controlled by settings.py
# if turned on, their urls will be added. (development)
# if turned off, no urls to the admin pages or the debug toolbar is added.
if settings.ADMIN_ENABLED:
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
        ] + urlpatterns


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
