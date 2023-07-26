import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message

# noinspection PyUnresolvedReferences

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Code to handle connection, authentication, etc.
        # For example, you can check user authentication here.

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Code to handle WebSocket disconnection
        pass

    async def receive(self, text_data):
        # Code to handle incoming WebSocket messages
        # For example, you can process the message, save it to the database, and broadcast it to other users.

        data = json.loads(text_data)
        message = data['message']
        user = self.scope['user']

        # Save the message to the database
        await self.save_message(user, message)

        # Send the message back to the client
        await self.send(text_data=json.dumps({
            'message': message,
            'username': user.username,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }))

    @database_sync_to_async
    def save_message(self, user, message):
        # Save the message to the database
        return Message.objects.create(user=user, content=message)
