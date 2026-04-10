from schema import PlannerOutput
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You structure topics."),
    ("human", "Break '{topic}' into 4-6 subtopics.")
])

structured_llm = llm.with_structured_output(PlannerOutput)

def planner_node(state):
    messages = prompt.format_messages(topic=state["topic"])

    response = structured_llm.invoke(messages)

    return {
        **state,
        "subtopics": response.subtopics
    }