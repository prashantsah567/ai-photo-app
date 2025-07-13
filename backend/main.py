from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api import process_image_replicate
from pathlib import Path
from app.api import generate_runpod

app = FastAPI()

from dotenv import dotenv_values
config = dotenv_values("backend/.env")  # returns a dict
print("Config",config.values)

# CORS setup for local frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message":"Backend running"}

# enables all POST requests
app.include_router(process_image_replicate.router)
app.include_router(generate_runpod.router)