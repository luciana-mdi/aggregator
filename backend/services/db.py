from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "aggregator")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]  # THIS is the variable being imported
