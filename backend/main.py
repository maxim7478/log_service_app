import json
import uuid
from fastapi import FastAPI, Request, HTTPException, WebSocketDisconnect, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from services.logs.api import logs_router
from services.logs.ws_api import lifespan, logs_ws_router

app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(logs_router)
app.include_router(logs_ws_router)