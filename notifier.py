import telebot
from config import TELEGRAM_TOKEN, ADMIN_CHAT_ID

class Notifier:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)
        
    def send_alert(self, message):
        if not message or not isinstance(message, str):
            print("⚠️ Invalid message format.")
            return
        try:
            self.bot.send_message(ADMIN_CHAT_ID, f"⚠️ ALERT: {message}")
        except Exception as e:
            print(f"⚠️ Failed to send alert: {e}")