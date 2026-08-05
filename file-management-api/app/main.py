from fastapi import FastAPI
from pydantic import BaseModel
import requests


app = FastAPI()


class AskRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "DevOps Accelerator AI API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_ai(data: AskRequest):

    response = requests.post(
        "http://host.docker.internal:11434/api/generate",
        json={
            "model": "gemma3:1b",
            "prompt": data.question,
            "stream": False
        },
        timeout=120
    )

    result = response.json()

    return {
        "question": data.question,
        "answer": result["response"]
    }
