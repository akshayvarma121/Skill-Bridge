from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
import logging
import traceback

from app.services.mongodb import connect_to_mongo, close_mongo_connection
from app.api.routes import router as api_router

logging.basicConfig(level=logging.DEBUG)

# --- FastAPI Lifespan for Startup/Shutdown ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()

app = FastAPI(
    title="Skill Bridge AI Assistant",
    lifespan=lifespan
)

# --- Add Error-Printing Middleware *after* app is created ---
@app.middleware("http")
async def print_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        print("EXCEPTION CAUGHT IN MIDDLEWARE:")
        traceback.print_exc()
        raise exc

# --- CORS Settings ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://skill-bridge-qdozmjwa4-akshayvarma121s-projects.vercel.app",
        "https://skill-bridge-ten-dusky.vercel.app",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include Routers ---
app.include_router(api_router, prefix="/api")

# --- API Endpoints ---
class VoiceInputPayload(BaseModel):
    text: str
    language: str

@app.get("/")
async def root():
    return {"message": "SkillBridge assistant is running!"}

@app.post("/voice-input")
async def handle_voice_input(payload: VoiceInputPayload):
    print(f"Received voice input ({payload.language}): '{payload.text}'")
    return {"processedText": payload.text}
