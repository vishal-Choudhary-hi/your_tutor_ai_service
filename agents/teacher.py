from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from schema import TeacherOutput

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a great teacher."),
    ("human", "Explain the topic '{topic}' simply with examples."),
    ("system","Instructions provided by the human '{instructions}' ")
])

structured_llm = llm.with_structured_output(TeacherOutput)

def teacher_node(state):
    messages = prompt.format_messages(topic=state["topic"], instructions=state["instructions"])

    response = structured_llm.invoke(messages)

    return {
        **state,
        "overview": response.overview
    }