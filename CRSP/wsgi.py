"""
WSGI config for CRSP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

# from django.core.wsgi import get_wsgi_application

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRSP.settings')

# application = get_wsgi_application()

application = get_asgi_application()
