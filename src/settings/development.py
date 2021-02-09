# import os
from .common import *

DEBUG = True
ALLOWED_HOSTS = []

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
