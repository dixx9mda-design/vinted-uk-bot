# vinted_scanner.py
import requests
from Config import telegram_bot_token, telegram_chat_id

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {"chat_id": telegram_chat_id, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Erreur Telegram:", e)

if __name__ == "__main__":
    # Test simple : envoie un message toutes les 15 secondes
    import time
    while True:
        send_telegram_message("Bot Vinted Test ✅ fonctionne !")
        time.sleep(15)
