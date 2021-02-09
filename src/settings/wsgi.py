"""
WSGI config for settings project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dj_static import Cling

from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('~/tourismapi')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.development')

application = Cling(get_wsgi_application())
