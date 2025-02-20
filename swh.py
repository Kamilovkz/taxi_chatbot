import requests
from dotenv import load_dotenv
import os

load_dotenv()


TG_API = os.getenv("BOT_API_KEY")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")

whook = "https://50c0-45-8-117-106.ngrok-free.app"

r = requests.get(f"https://api.telegram.org/bot{TG_API}/setWebhook?url={whook}/")

print(r.json())
