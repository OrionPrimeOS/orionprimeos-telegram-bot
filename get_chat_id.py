import requests

bot_token = "8341616041:AAFpd83O03wD30xa3xFMW2K0TrLI8RYq8d4"
url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

resp = requests.get(url).json()
print(resp)
