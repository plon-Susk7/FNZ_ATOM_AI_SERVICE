from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from google import genai
import os
from dotenv import load_dotenv
from services.llm import ChatGraph

load_dotenv()
router = APIRouter()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.websocket("/ws/chat")
async def model_conversation(websocket : WebSocket):

    await websocket.accept()

    chat = ChatGraph()
    try:
        while True:
            user_text = await websocket.receive_text()
            result = chat.invoke(user_text)
            message = result.get("messages", [])[-1]
            await websocket.send_text(message.content)
    except WebSocketDisconnect:
        print("Client disconnected")
