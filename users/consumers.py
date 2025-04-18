import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatMessage
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "dispatchers"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        user_name = text_data_json.get('user_name', 'Anonim')

        # Xabarni bazaga saqlash
        await self.save_message(user_name, content)

        # Xabarni guruhdagi barcha foydalanuvchilarga yuborish
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'content': content,
                'user_name': user_name,
                'created_at': timezone.now().isoformat()
            }
        )

    async def chat_message(self, event):
        # Xabarni WebSocket orqali yuborish
        await self.send(text_data=json.dumps({
            'content': event['content'],
            'user_name': event['user_name'],
            'created_at': event['created_at']
        }))

    @database_sync_to_async
    def save_message(self, user_name, content):
        ChatMessage.objects.create(
            user_name=user_name,
            content=content,
            user=self.scope['user'] if self.scope['user'].is_authenticated else None
        )
