"""
ASGI config for settings project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

application = get_asgi_application()
