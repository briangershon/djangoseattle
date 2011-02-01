
Welcome to the Django Seattle website project.

GETTING STARTED
---------------
1. To get started with this project, create a ./src/settings_local.py file
with just an import line to an existing local dev settings file:

from settings.dev import *

2. Install Django-Basic app listed below in the list of Dependencies.

3. Run "manage.py syncdb" to create models

4. Run "manage.py runserver" to see a working site


USING DJANGO DEBUG TOOLBAR
--------------------------

1. Clone the Django Debug Toolbar repository:
git clone "git://github.com/robhudson/django-debug-toolbar.git"

2. Install it:
python django-debug-toolbar/setup.py install

3. Add the following lines to your settings_local.py file.

from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

4. Enjoy. More documentation here: http://github.com/robhudson/django-debug-toolbar/tree/master

USING TWITSEARCH
----------------

1. Add "twitsearch.context_processors.tweets" to TEMPLATE_CONTEXT_PROCESSORS in settings

2. Include "twitsearch/twit_include.html" in your template

3. Add TWITTER_SEARCH_URL = 'http://search.twitter.com/search.json?' to your settings

4. ????

5. Profit!

DEPENDENCIES
------------
REQUIRES Python 2.5 (2.5 specific code in handytags.py)

1. django-basic-apps:
svn checkout http://django-basic-apps.googlecode.com/svn/trunk/ basic

1a. python-dateutil
easy_install python-dateutil
or
http://pypi.python.org/pypi/python-dateutil

1b. markdown
easy_install markdown
or
http://pypi.python.org/pypi/Markdown

1c. django-tagging:
svn checkout http://django-tagging.googlecode.com/svn/trunk/tagging tagging

2. httplib2
    Needed by twitsearch
    http://code.google.com/p/httplib2/

    $ easy_install httplib2
