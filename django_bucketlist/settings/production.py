from .base import *

import dj_database_url

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

BOWER_PATH = '/app/node_modules/bower'

DATABASES['default']['CONN_MAX_AGE'] = 500

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'