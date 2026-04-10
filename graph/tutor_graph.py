from langgraph.graph import StateGraph, END
from agents.planner import planner_node
from agents.quiz import quiz_node
from agents.teacher import teacher_node

def build_graph():
    builder = StateGraph(dict)

    builder.add_node("teacher", teacher_node)
    builder.add_node("planner", planner_node)
    builder.add_node("quiz", quiz_node)

    builder.set_entry_point("teacher")

    builder.add_edge("teacher", "planner")
    builder.add_edge("planner", "quiz")
    builder.add_edge("quiz", END)

    return builder.compile()