import os
from dotenv import load_dotenv

load_dotenv(".env.bot.secret")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
LMS_API_URL = os.getenv("LMS_API_URL", "http://localhost:8000")
LMS_API_KEY = os.getenv("LMS_API_KEY", "")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")