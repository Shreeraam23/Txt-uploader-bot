import os

API_ID    = os.environ.get("API_ID", "20373203")
API_HASH  = os.environ.get("API_HASH", "8962717c7c708e210f66ea658db58d85")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7843117240:AAG23JIBWgbn82AZLL7IODPLg7an3bBESik") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
