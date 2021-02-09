"""
WSGI config for settings project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('~/tourismapi')

load_dotenv()
print(os.getenv('DJANGO_SETTINGS_MODULE'))

os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

application = Cling(get_wsgi_application())
