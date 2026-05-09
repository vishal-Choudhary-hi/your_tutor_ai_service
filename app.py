import logging
import os

from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
from graph.tutor_graph import build_graph

app = FastAPI()
graph = build_graph()


class TutorRequest(BaseModel):
    topic: str
    instructions: str

API_KEY = os.getenv("INTERNAL_API_KEY")


def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/generate")
def generate_tutor(req: TutorRequest, api_key: str = Depends(verify_api_key)):
    state = {
        "topic": req.topic,
        "instructions": req.instructions
    }

    result = graph.invoke(state)

    return result