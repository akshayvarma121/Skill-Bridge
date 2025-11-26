from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager

from app.services.mongodb import connect_to_mongo, close_mongo_connection
from app.api.routes import router as api_router

# Optional Redis imports for future use
# from app.services.redis_client import connect_to_redis, close_redis_connection
# from app.api import voice

# --- Pydantic Models ---
class VoiceInputPayload(BaseModel):
    text: str
    language: str

class UserProfile(BaseModel):
    name: str
    skills: list[str]
    education: str
    location: str

# --- FastAPI Lifespan for Startup/Shutdown ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    await connect_to_mongo()
    # Uncomment if Redis is configured and used:
    # await connect_to_redis()
    yield
    # Shutdown actions
    await close_mongo_connection()
    # Uncomment if Redis is configured and used:
    # await close_redis_connection()

app = FastAPI(
    title="Skill Bridge AI Assistant",
    lifespan=lifespan
)

# --- CORS Settings ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://skill-bridge-qdozmjwa4-akshayvarma121s-projects.vercel.app",
        "https://skill-bridge-ten-dusky.vercel.app",
        "http://localhost:5173"
    ],  # add your Vercel frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include Routers ---
app.include_router(api_router, prefix="/api")

# --- API Endpoints ---
@app.get("/")
async def root():
    return {"message": "SkillBridge assistant is running!"}

@app.post("/voice-input")
async def handle_voice_input(payload: VoiceInputPayload):
    print(f"Received voice input ({payload.language}): '{payload.text}'")
    return {"processedText": payload.text}

# Place this file at the entrypoint of your FastAPI backend (where your Render deployment expects).
