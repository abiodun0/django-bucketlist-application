from .base import *

import dj_database_url

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

BOWER_PATH = '/app/node_modules/bower'

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']