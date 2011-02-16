Welcome to the Django Seattle website project.

GETTING STARTED
---------------
* Setup a virtual environment with Python 2.x (tested on Python 2.5)

	e.g.

	export PIP_REQUIRE_VIRTUALENV=true
	export PIP_RESPECT_VIRTUALENV=true

	cd /your-desired-virtualenv-folder
	virtualenv --no-site-packages djangoseattle_env
	cd djangoseattle_env
	source bin/activate
	./bin/easy_install pip
	git clone git://github.com/briangershon/djangoseattle.git
	./bin/pip install -r requirements.txt

* Create a site

	./bin/django-admin.py createproject site
	cd site
	chmod u+x manage.py
	Test that mange.py works: ./manage.py help

* To get started with this project, create a ./src/settings_local.py file
with just an import line to an existing local dev settings file:

	from settings.dev import *

* Run `manage.py syncdb` to create models

* Run `manage.py runserver` to see a working site


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