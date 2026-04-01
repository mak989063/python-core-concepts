# FastAPI + MCP One-Page Cheat Sheet (Ready Code)

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import time
import uuid

app = FastAPI()

# -------------------------------
# Input Model
# -------------------------------
class Input(BaseModel):
    text: str


# -------------------------------
# Middleware (Important)
# -------------------------------
@app.middleware("http")
async def middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.time()

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time"] = str(time.time() - start)

    return response


# -------------------------------
# POST Endpoint
# -------------------------------
@app.post("/analyze")
async def analyze(data: Input):
    text = data.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Empty input")

    words = text.split()

    return {
        "word_count": len(words),
        "char_count": len(text),
        "uppercase": text.upper()
    }


# -------------------------------
# GET Endpoint
# -------------------------------
@app.get("/")
async def home():
    return {"message": "API working"}


# -------------------------------
# Run Command (use in terminal)
# -------------------------------
# uvicorn main:app --reload