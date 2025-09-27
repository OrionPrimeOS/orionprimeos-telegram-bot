from flask import Flask, request
from dotenv import load_dotenv
import os, requests

# Load .env values
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
VIP_ID = os.getenv("TELEGRAM_VIP_CHAT_ID")
CONTROL_ID = os.getenv("CONTROL_CHAT_ID")

TG_API = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

# --- Health Check ---
@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "message": "OrionPrimeOS is running"}, 200

# --- Telegram Webhook ---
@app.route(f"/{TOKEN}", methods=["POST"])
def telegram_webhook():
    update = request.get_json(force=True)
    chat_id = update.get("message", {}).get("chat", {}).get("id")
    text = update.get("message", {}).get("text", "")

    if text:
        msg = f"Echo from OrionPrimeOS: {text}"
        requests.post(f"{TG_API}/sendMessage", json={"chat_id": chat_id, "text": msg})

    return "ok", 200

# --- TradingView Webhook ---
@app.route("/tv", methods=["POST"])
def tradingview_webhook():
    data = request.get_json(force=True) or {}
    pair = data.get("pair", "XAUUSD")
    direction = data.get("direction", "n/a")
    entry = data.get("entry", "")
    sl = data.get("sl", "")
    tp = data.get("tp", "")

    msg = (
        f"⚡ OrionPrimeOS Signal ⚡\n"
        f"Pair: {pair}\n"
        f"Direction: {direction}\n"
        f"Entry: {entry}\nSL: {sl}\nTP: {tp}"
    )

    if VIP_ID:
        requests.post(f"{TG_API}/sendMessage", json={"chat_id": VIP_ID, "text": msg})

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
