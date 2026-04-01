from fastapi import FastAPI, HTTPException

app = FastAPI()
data = {
  "name": "manikandan",
  "city": "bangalore"
}
@app.post("/process")
async def process(data: dict):
    if not data:
        raise HTTPException(status_code=400, detail="Empty input")

    result = {k: str(v).upper() for k, v in data.items()}

    return {
        "input": data,
        "output": result
    }
