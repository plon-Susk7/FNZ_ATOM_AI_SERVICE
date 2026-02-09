from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from google import genai
import os
from dotenv import load_dotenv
from app.services.llm import ChatGraph

load_dotenv()
router = APIRouter()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@router.get("/")
def read_root():
    return {"Hello": "World"}

# @router.get("/available_bsd")
# def get_available_bsd():
#     list_bsd = os.listdir("app/bsd")
#     return {"available_bsd": list_bsd}

# @router.get("/get_stories/{bsd_name}")
# def get_stories(bsd_name: str):
#     bsd_path = f"app/bsd/{bsd_name}"
#     if not os.path.exists(bsd_path):
#         return {"error": "BSD not found"}
#     stories = os.listdir(bsd_path)
#     return {"stories": stories}

@router.get("/api/chat/start/{project_uri}")
def get_project_context_path(project_uri: str):
    return {"context_path": f"app/bsd/{project_uri}/US1 - NMPA Product Registration & Compliance System (PRCS)"}


@router.get("/get_story_content/{context_path}")
def get_story_content(context_path: str):
    story_path = context_path
    if not os.path.exists(story_path):
        return {"error": "Story not found"}
    with open(story_path, "r") as f:
        content = f.read()
    return {"content": content}

@router.websocket("/ws/api/chat/{context_path:path}")
async def model_conversation(websocket : WebSocket, context_path: str):

    await websocket.accept()
    pre_context_bsd = get_story_content(context_path)
    chat = ChatGraph(pre_context=pre_context_bsd["content"])
    try:
        while True:
            user_text = await websocket.receive_text()
            result = chat.invoke(user_text)
            message = result.get("messages", [])[-1]
            await websocket.send_text(message.content)
    except WebSocketDisconnect:
        print("Client disconnected")


