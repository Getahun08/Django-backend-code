"""
ASGI config for Emgs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
settins_module='Emgs.Deployement' if 'WEPSITE_HOSTNAME'in os.environ else'Emgs.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settins_module)

application = get_asgi_application()
