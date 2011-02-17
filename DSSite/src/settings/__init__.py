import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)[0: (os.path.dirname(__file__).rindex(os.sep + 'src' + os.sep))])

SERVER_EMAIL = ''
##### Admin
ADMIN_MEDIA_PREFIX = '/static/admin/'

##### Accounts
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

##### Core
LANGUAGE_CODE = 'en-us'
USE_I18N = False
ROOT_URLCONF = 'urls'
SECRET_KEY = '@#$@^#@%(tafdsafasla*&*$fds@((*^tltdq5p1gu'

##### Templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'twitsearch.context_processors.tweets',
)

##### Installed
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
	  'django.contrib.markup',
	  'django.contrib.comments',
	  'tagging',
    'dssite',
	  'basic.*',
)

SITE_ID = 1

TWITTER_SEARCH_URL = 'http://search.twitter.com/search.json?'

from settings_local import * #@UnusedWildImport
