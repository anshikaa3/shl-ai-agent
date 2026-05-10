from fastapi import FastAPI
from app.models import ChatRequest
from app.agent import process_chat

app = FastAPI()

@app.get("/health")
def health():

    return {
        "status": "ok"
    }

@app.post("/chat")
def chat(req: ChatRequest):

    return process_chat(req.messages)