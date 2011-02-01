from django.conf.urls.defaults import *

from twitsearch.views import home

urlpatterns = patterns('',
    url(r'^$', home, name='twit_home'),
 )