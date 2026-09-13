from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from db import save_incident

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Hello, AI Agent!"}

@app.post("/chat/")
async def create_chat(item: ChatRequest):
    save_incident(item.message)
    
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8080/incident")
        print("Response from Go service:", response.text)

    return {"response": f"You said: {item.message}"}
