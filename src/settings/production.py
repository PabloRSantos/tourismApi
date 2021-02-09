import os
from .common import *


DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'public'),
        'USER': os.getenv('POSTGRES_USER', 'root'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'root'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
    }
}
