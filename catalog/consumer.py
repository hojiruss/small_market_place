import json
from channels.generic.websocket import WebsocketConsumer


class OrdersConsumer(WebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message":"connected"}))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
