"""
WSGI config for TreloSinc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import inject
from django.core.wsgi import get_wsgi_application

from TreloSinc.inject import config_inject

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TreloSinc.settings')

application = get_wsgi_application()

# Configure dependency injection

inject.configure_once(config_inject)
