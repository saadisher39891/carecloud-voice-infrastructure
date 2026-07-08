from fastapi import FastAPI, Request
from loguru import logger
import json
from datetime import datetime

app = FastAPI(title="CareCloud Voice Agent Backend")

# Configure structured logging
logger.add("logs/app.log", rotation="1 day", retention="7 days", format="{time} {level} {message}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.post("/webhook")
async def vapi_webhook(request: Request):
    body = await request.json()
    logger.info(f"Webhook received: {json.dumps(body)}")
    return {"status": "received"}

@app.post("/call-started")
async def call_started(request: Request):
    body = await request.json()
    logger.info(f"Call started: {body}")
    return {"status": "ok"}

@app.post("/call-ended")
async def call_ended(request: Request):
    body = await request.json()
    logger.info(f"Call ended: {body}")
    return {"status": "ok"}