from datetime import datetime

from fastapi import WebSocket
from services.logs.api_func import tail_file


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


class Scheduler:
    def __init__(self):
        self.dict_clients: dict = {}

    def add_client(self, client):
        self.dict_clients[client.id] = client

    def remove(self, client_id):
        del self.dict_clients[client_id]

    async def send_data(self, manager):
        current_key = None
        try:
            for key in self.dict_clients:
                current_key = key
                websocket = self.dict_clients[key].websocket
                count_rows = self.dict_clients[key].count_rows
                arr = tail_file('files/test.log', int(count_rows))
                now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

                message = {
                    "id": key,
                    "logs": arr,
                    "date_time": now,
                }

                await manager.send_message(message, websocket)
        except Exception:
            if current_key:
                self.remove(current_key)


class Client:
    def __init__(self, client_id, websocket: WebSocket, count_rows: int):
        self.id: str = client_id
        self.websocket: WebSocket = websocket
        self.count_rows: int = count_rows
