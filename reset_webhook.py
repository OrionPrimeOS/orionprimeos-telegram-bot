import requests, os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BASE = os.getenv("BASE_URL")

if not TOKEN or not BASE:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or BASE_URL in .env")

delete_url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
set_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={BASE}/{TOKEN}"
info_url = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"

print("Deleting old webhook...")
print(requests.get(delete_url).text)

print("Setting new webhook...")
print(requests.get(set_url).text)

print("Webhook info:")
print(requests.get(info_url).text)
