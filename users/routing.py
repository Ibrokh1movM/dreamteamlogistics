from django.urls import re_path
from users.views import DispatcherConsumer

websocket_urlpatterns = [
    re_path(r'ws/dispatchers/$', DispatcherConsumer.as_asgi()),
]
