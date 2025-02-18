import os
from dotenv import load_dotenv
import requests

load_dotenv()

TG_API = os.getenv("BOT_API_KEY")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")

data = {
    "chat_id": ADMIN_ID,
    "text": "Hello World",
}

req = requests.post(f"https://api.telegram.org/bot{TG_API}/sendMessage", data=data)
print(req.status_code)
