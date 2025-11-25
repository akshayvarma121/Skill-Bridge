from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:/Users/varma/Desktop/skill bridge/backend/app/.env")


MONGO_URI = os.getenv("MONGO_URI")
print(MONGO_URI)

async def connect_to_mongo():
    global _client, _db
    _client = AsyncIOMotorClient(MONGO_URI)
    _db = _client["ai_assistant"]   # specify db name
    print("✅ Connected to MongoDB Atlas:", _db.name)

async def close_mongo_connection():
    global _client
    if _client:
        _client.close()
        print("❌ MongoDB connection closed")

def get_db():
    """
    Dynamically return the database object.
    Raises exception if MongoDB is not initialized yet.
    """
    if _db is None:
        raise Exception("MongoDB connection not initialized")
    return _db
