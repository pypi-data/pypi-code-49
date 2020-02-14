from django.conf.urls import url, include
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from aparnik.middlewares.token_auth import TokenAuthMiddlewareStack
from aparnik.contrib.messaging.consumers import MessagingConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        TokenAuthMiddlewareStack(
            URLRouter(
                [
                    url(r'^messaging/', MessagingConsumer),
                ]
            )
        )
    )
})
