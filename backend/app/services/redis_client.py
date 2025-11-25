import os
from dotenv import load_dotenv
import redis.asyncio as redis

load_dotenv(dotenv_path="C:/Users/varma/Desktop/skill bridge/backend/app/.env")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = 17487      # Ensure this is always an int
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

print("Redis Host:", REDIS_HOST)
print("Redis Port:", REDIS_PORT)
print("Redis Password:", REDIS_PASSWORD)

redis_client: redis.Redis | None = None

async def connect_to_redis():
    global redis_client
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
    try:
        await redis_client.ping()
        print("✅ Connected to Redis")
    except Exception as e:
        print("❌ Redis connection failed:", e)

async def close_redis_connection():
    global redis_client
    if redis_client:
        await redis_client.close()
        print("❌ Redis connection closed")
