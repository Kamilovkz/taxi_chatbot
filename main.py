from fastapi import FastAPI
import uvicorn
from schemas import Answer
from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

TG_API = os.getenv("BOT_API_KEY")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")

app = FastAPI()


@app.post("/")
async def read_root(obj: Answer):
    # TODO: here we can make more universal it, via creating a complex schemas with all type of message in telegram
    if obj.message.photo is not None:
        data = {"chat_id": ADMIN_ID, "photo": obj.message.photo[-1].file_id}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"https://api.telegram.org/bot{TG_API}/sendPhoto", data=data
            ) as response:
                return response.status

    else:
        data = {"chat_id": ADMIN_ID, "text": obj.message.text}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"https://api.telegram.org/bot{TG_API}/sendMessage", data=data
            ) as response:
                return response.status
    return {"ok": "work"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="localhost", reload=True)
