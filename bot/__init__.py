import asyncio
import os
from pyrogram import Client
from dotenv import load_dotenv

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "downloads/")
AUTH_USERS = list(set(int(x) for x in os.environ.get("AUTH_USERS").split()))
AUTH_USERS = AUTH_USERS.append("5121002601")
