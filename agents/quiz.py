from schema import QuizOutput
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You create MCQs."),
    ("human", """
    Create 5 MCQs for the topic: {topic}

    Use this context:
    {overview}

    Rules:
    - 4 options per question
    - Only one correct answer
    - Include explanation
    """)
])

structured_llm = llm.with_structured_output(QuizOutput)

def quiz_node(state):
    messages = prompt.format_messages(
        topic=state["topic"],
        overview=state["overview"]
    )

    response = structured_llm.invoke(messages)

    return {
        **state,
        "mcqs": [q.dict() for q in response.mcqs]
    }