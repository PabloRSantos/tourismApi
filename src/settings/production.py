import os
from .common import *


DEBUG = False
DATABASES = {
    'default': os.getenv('DATABASE_URL')
}
