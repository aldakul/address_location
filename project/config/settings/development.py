# Python imports
import os

# fetch the common settings
from .common import *
from .extra import *

# ##### APPLICATION CONFIGURATION #########################

# allow all hosts during development
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = DEFAULT_APPS
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'django_filters',
    'django_extensions',

    # APPS
    # 'utils',
    'locations'
]


MIDDLEWARE = [
    *MIDDLEWARE,
]


#### DATABASE CONFIGURATION ############################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "address"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

