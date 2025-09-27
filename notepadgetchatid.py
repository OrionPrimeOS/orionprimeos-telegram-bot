import requests

bot_token = "8341616041:AAFpd830O3wD30xa3xFMV2K0TrLI8RYq8d4"  # your token
url = f"https://api.telegram.org/bot{bot_token}/getUpdates?offset=-1"
resp = requests.get(url).json()
print(resp)
