from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

@app.post("/v1/chat/completions")
async def chat_completion(request: Request):
    data = await request.json()
    api_key = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not api_key:
        return {"error": "Missing API Key in Authorization header"}

    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model=data.get("model", "gpt-3.5-turbo"),
            messages=data.get("messages", []),
            temperature=data.get("temperature", 1.0)
        )
        return response
    except Exception as e:
        return {"error": str(e)}
