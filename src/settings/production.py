import os
from .common import *


DEBUG = False
DATABASES = {
    'default': os.getenv('DATABASE_URL')
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
