# Python imports
from pathlib import Path
from .extra import *
import os
import logging
import sys

logger = logging.getLogger(__name__)

# ##### PATH CONFIGURATION ################################

# fetch Django's project directory
DJANGO_ROOT = Path(__file__).resolve(strict=True).parent.parent

# fetch the project_root
PROJECT_ROOT = DJANGO_ROOT.parent

# the name of the whole site
SITE_NAME = DJANGO_ROOT.name

# collect static files here
STATIC_ROOT = PROJECT_ROOT / 'staticfiles'

# the URL for static files
STATIC_URL = '/staticfiles/'

# look for static assets here
STATICFILES_DIRS = [
    PROJECT_ROOT / 'static',
]

# collect media files here
MEDIA_ROOT = PROJECT_ROOT / 'media'

# the URL for media files
MEDIA_URL = '/media/'

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    PROJECT_ROOT / 'templates',
]

# add apps/ to the Python path
sys.path.append(str(PROJECT_ROOT / 'apps'))

# ##### APPLICATION CONFIGURATION #########################


# set the project's default timezone
TIME_ZONE = os.environ.get('DPS_TIMEZONE', 'Asia/Almaty')

# these are the apps
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# The WSGI application to be used by Django's internal servers.
# Please note, Django's 'runserver' should **not** be used in production
# environments.
# If set to 'None', 'django.core.wsgi.get_wsgi_application()' will be used to
# determine the WSGI application.
WSGI_APPLICATION = os.environ.get('DPS_DJANGO_WSGI_APP', None)

# the root URL configuration
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)

# adjust the minimal login
# LOGIN_URL = 'core_login'
# LOGIN_REDIRECT_URL = os.environ.get('DPS_DJANGO_LOGIN_REDIRECT_URL', '/')
# LOGOUT_REDIRECT_URL = os.environ.get('DPS_DJANGO_LOGOUT_REDIRECT_URL', 'core_login')

# Internationalization
USE_I18N = False

# uncomment the following line to include i18n
from .i18n import *

# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
SECRET_FILE = str(PROJECT_ROOT / 'run' / 'SECRET.key')

# these persons receive error notification
ADMINS = (
    ('B. Aldakulov', 'bauyrzhanaldakulov@gmail.com'),
)
MANAGERS = ADMINS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ##### DEBUG CONFIGURATION ###############################
DEBUG = False

SECRET_KEY = os.environ.get('DPS_DJANGO_SECRET_KEY')

if SECRET_KEY is None:
    logger.debug('Could not find key in the environment!')

    logger.debug('Trying to read SECRET_KEY from SECRET_FILE...')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
        logger.info('Read SECRET_KEY from SECRET_FILE.')
    except IOError:
        logger.debug('Could not open SECRET_FILE ({})!'.format(SECRET_FILE))

        try:
            from django.utils.crypto import get_random_string

            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
            SECRET_KEY = get_random_string(50, chars)
            with open(SECRET_FILE, 'w') as f:
                f.write(SECRET_KEY)

            logger.info('Generated a new SECRET_KEY and stored it in SECRET_FILE ({})!'.format(SECRET_FILE))
        except IOError:
            logger.exception('Could not open SECRET_FILE ({}) for writing!'.format(SECRET_FILE))
            raise Exception('Could not open {} for writing!'.format(SECRET_FILE))
else:
    logger.info('Fetched SECRET_KEY from environment.')

# LOGGING
# ---------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console"]},
    "formatters": {
        "verbose": {
            "format": (
                "[%(asctime)s] %(levelname)s %(name)s %(message)s [PID:%(process)d:%(threadName)s]"
            )
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING',  # DEBUG will log all queries, so change it to WARNING.
            'propagate': False,  # Don't propagate to other handlers
        },
        "dms_new": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True
        },
    },
}
