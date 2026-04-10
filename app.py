from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
from graph.tutor_graph import build_graph

app = FastAPI()
graph = build_graph()


class TutorRequest(BaseModel):
    topic: str
    instructions: str


@app.post("/generate")
def generate_tutor(req: TutorRequest):
    state = {
        "topic": req.topic,
        "instructions": req.instructions
    }

    result = graph.invoke(state)

    return result