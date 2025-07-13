from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import process_image
from pathlib import Path

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

# enables the new POST /api/process route
app.include_router(process_image.router)