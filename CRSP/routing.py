from django.urls import path
from accounts.consumers import ChatConsumer
# from CRSP.routing import application


websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]
