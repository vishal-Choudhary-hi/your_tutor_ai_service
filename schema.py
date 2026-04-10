from pydantic import BaseModel
from typing import List

class MCQ(BaseModel):
    question: str
    options: List[str]
    correct_answer_index: int
    explanation: str

class TeacherOutput(BaseModel):
    overview: str

class PlannerOutput(BaseModel):
    subtopics: List[str]

class QuizOutput(BaseModel):
    mcqs: List[MCQ]