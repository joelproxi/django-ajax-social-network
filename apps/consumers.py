
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from apps.serializers import NotificationSerialiser

from .models import Notification


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'notification'
        await self.accept()
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.send(text_data=json.dumps({"message": "Hello proxi"}))
        

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        pass

    async def receive(self, text_data):
        print(text_data)
        message = "hello"
        event = {
            "type": "send_notif",
            "message": "hello"
        }
        await self.channel_layer.group_send(self.group_name, event)
        # await self.send(text_data=json.dumps({"message": message}))

    async def send_notif(self, event):
        data = await self.get_notif_from_db()
        await self.send(text_data=data)
      
    @database_sync_to_async    
    def get_notif_from_db(self):
        notif_list = Notification.objects.all()
        serializer = NotificationSerialiser(notif_list, many=True)
        return json.dumps(serializer.data)
        
        