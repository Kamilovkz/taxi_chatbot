from fastapi import FastAPI, Request
import uvicorn
from schemas import Answer
from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

TG_API = os.getenv("BOT_API_KEY")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")

app = FastAPI()


@app.post("/answer")
async def answer(chat_id: str, text: str):
    data = {
        "chat_id": chat_id,
        "text": text,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api.telegram.org/bot{TG_API}/sendMessage", data=data
        ) as response:
            return response.status


@app.post("/")
async def read_root(obj: Answer):
    # request: Request
    # result = await request.json()
    # obj = Answer.model_validate(result)
    data = {"chat_id": ADMIN_ID, "text": obj.message.text}
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api.telegram.org/bot{TG_API}/sendMessage", data=data
        ) as response:
            return response.status

    return {"ok": "work"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="localhost", reload=True)
