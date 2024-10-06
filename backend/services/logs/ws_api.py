import datetime
import json
import uuid
from contextlib import asynccontextmanager

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from pytz import utc

from services.logs.api_func import tail_file
from services.logs.models import Client, ConnectionManager, Scheduler

scheduler = AsyncIOScheduler(timezone=utc)

manager = ConnectionManager()
scheduler_obj = Scheduler()

logs_ws_router = APIRouter(
    prefix="/ws-logs"
)


async def send_logs():
    await scheduler_obj.send_data(manager)


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    scheduler.add_job(send_logs, "interval", seconds=5)
    yield


@logs_ws_router.websocket("/")
async def get_logs_ws_api(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            client_data = await websocket.receive_text()
            client_data = json.loads(client_data)
            client_id = client_data['id']
            count_rows = client_data['lines']

            if client_id is None:
                client_id = str(uuid.uuid4())
                client = Client(client_id, websocket, int(count_rows))
                scheduler_obj.dict_clients[client.id] = client

            scheduler_obj.dict_clients[client_id].count_rows = int(count_rows)

            arr = tail_file('files/test.log', int(count_rows))
            now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            message_data = {
                "id": client_id,
                "logs": arr,
                "date_time": now,
            }
            await manager.send_message(message_data, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Connection closed")
