"""
ASGI config for Studybuddy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import chat_app.route
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Studybuddy.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
     'websoc' : AuthMiddlewareStack(
         URLRouter(
             chat_app.route.websoc_urlpatterns
         )
     )
})
