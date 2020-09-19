import os

class Config:
    LICENSE_KEY = os.environ.get("LICENSE_KEY")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOG_CHAT_ID = os.environ.get("LOG_CHAT_ID")