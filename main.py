from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import json
import os
# Import your existing logic
from training import main_pipeline

app = FastAPI()

# CORS setup (allow from your Vercel frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DigestRequest(BaseModel):
    url: str
    direction: str

@app.post("/generator")
async def generate_digest(request: DigestRequest):
    result = main_pipeline(request.url, request.direction)
    return result  # should be a dict (FastAPI will convert to JSON)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
