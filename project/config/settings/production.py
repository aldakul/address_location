# # Python imports
# import os
#
# # fetch the common settings
# from .common import *
#
#
# # ##### APPLICATION CONFIGURATION #########################
#
# # You will have to determine, which hostnames should be served by Django
# # Determines, which hostnames should be served by Django.
# # DPS_DJANGO_ALLOWED_HOSTS may contain a list of (acceptable) hostnames, while
# # DPS_SERVER_NAME may only contain one hostname, as this value also determines
# # the actual hostname, that is used by Nginx.
# #
# # If neither DPS_DJANGO_ALLOWED_HOSTS nor DPS_SERVER_NAME are provided, this
# # will be an empty list and thus, no host will be served, rendering Django
# # effectively useless.
# ALLOWED_HOSTS = ['*']
#
# INSTALLED_APPS = DEFAULT_APPS
# INSTALLED_APPS += [
#     'corsheaders',
#     'rest_framework'
# ]
#
# MIDDLEWARE = [
#     *MIDDLEWARE,
# ]
#
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql',
# #         'NAME': 'database_name',
# #         'USER': 'database_user',
# #         'PASSWORD': 'database_password',
# #         'HOST': 'db',
# #         'PORT': '5432',
# #     }
# # }
#
# # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
#
# # Don't let Django configure logging in a production environment.
# # Most probably, configuring logging should be done by WSGI Server, i.e.
# # Gunicorn or uWSGI.
# # For Docker-based deployments, logging is configured in 'gunicorn_conf.py'.
# #
# # Without setting LOGGING_CONFIG to 'None', Django will setup Python's logging
# # module, as described https://docs.djangoproject.com/en/3.0/topics/logging/#default-logging-configuration
#
# # LOGGING_CONFIG=None
#
# # ##### SECURITY CONFIGURATION ############################
#
# # TODO: Make sure, that sensitive information uses https
# # TODO: Evaluate the following settings, before uncommenting them
# # redirects all requests to https
# # SECURE_SSL_REDIRECT = True
# # session cookies will only be set, if https is used
# # SESSION_COOKIE_SECURE = True
# # how long is a session cookie valid?
# # SESSION_COOKIE_AGE = 1209600


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
    'utils',
]

MIDDLEWARE = [
    *MIDDLEWARE,
]

#### DATABASE CONFIGURATION ############################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True
