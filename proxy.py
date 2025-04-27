from fastapi import FastAPI, Request, HTTPException
import httpx
import os
from dotenv import load_dotenv

app = FastAPI()

if not os.getenv("PRODUCTION"):
    load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")

@app.middleware("http")
async def verify_token(request: Request, call_next):
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Invalid token.")
    response = await call_next(request)
    return response

@app.post("/v1/chat/completions")
async def proxy(request: Request):
    body = await request.body()
    headers = {"Content-Type": "application/json"}
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{API_URL}/v1/chat/completions", headers=headers, content=body, timeout=210)
    return resp.json()
