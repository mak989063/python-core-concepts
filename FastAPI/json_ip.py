#FastAPI + MCP One-Page Cheat Sheet
#1. Basic Setup
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import time, uuid
app = FastAPI()
#2. Input Model
class Input(BaseModel):
 text: str
#3. Middleware (Important)
@app.middleware("http")
async def middleware(request: Request, call_next):
 request_id = str(uuid.uuid4())
 start = time.time()
 response = await call_next(request)
 response.headers["X-Request-ID"] = request_id
 response.headers["X-Process-Time"] = str(time.time() - start)
 return response
#4. POST Endpoint
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
#5. GET Endpoint
@app.get("/")
async def home():
 return {"message": "API working"}
#6. Run
#uvicorn main:app --reload
#Remember: Input → Validate → Process → Return
#Always use async, BaseModel, middleware, and error handling.