# CORS HEADERS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['http://localhost', 'http://127.0.0.1']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with'
]

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30
}

CORE_BASE_URL = 'https://api.core.sandbox.mycarpro.net/'

AUTH_ALGORITHM = 'HS256'
AUTH_TOKEN_SECRET = 'secret'

# Always use IPython for shell_plus
SHELL_PLUS = "ipython"
