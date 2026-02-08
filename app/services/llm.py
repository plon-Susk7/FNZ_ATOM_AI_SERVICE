from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
import os
from dotenv import load_dotenv


class ChatGraph:

    def __init__(self):
        self.graph = self._build_graph()
        self.llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7, max_tokens=2048,google_api_key = os.getenv("GEMINI_API_KEY"))


    def _mock_llm(self, state: dict):

        messages = state["messages"]

        res = self.llm.invoke(messages)
        llm_response_message = res.content[0]['text']
        return {
                "messages": [{
                    "role": "ai",
                    "content":llm_response_message
                }]
            }


    def _build_graph(self):
        checkpointer = InMemorySaver()
        graph = StateGraph(MessagesState)

        graph.add_node("mock_llm", self._mock_llm)

        graph.add_edge(START, "mock_llm")
        graph.add_edge("mock_llm", END)

        return graph.compile(checkpointer=checkpointer)


    def invoke(self, user_message: str):

        return self.graph.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        },
        {"configurable":{"thread_id": "1"}}
        )
