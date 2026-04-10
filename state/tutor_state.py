from typing import TypedDict, Optional, List

class TutorState(TypedDict):
    topic: str
    plan: List[str]
    explanation: str
    quiz: List[str]
    answers: List[str]
    step: int
    instructions: str

