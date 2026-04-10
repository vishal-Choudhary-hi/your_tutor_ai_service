from dotenv import load_dotenv
import json

load_dotenv()
from graph.tutor_graph import build_graph

def main():
    graph = build_graph()

    topic = input("Enter topic: ")
    instructions= input("Enter any specific instructions for your tutor: ")
    state = {
        "topic": topic,
        "instructions": instructions
    }

    result = graph.invoke(state)

    print("\n📚 RESULT:\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()