# from fastapi import FastAPI
# from app.core.config import settings
# from app.routers import health, rag, ingestion

# app = FastAPI()

# app.include_router(health.router)
# app.include_router(rag.router)
# app.include_router(ingestion.router)

# @app.get("/")
# async def root():
#     return {"message": "RAG Chatbot Backend is running!"}

import sys
import os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import health, rag, ingestion

app = FastAPI()

# CORS configuration to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - restrict in production if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(rag.router)
app.include_router(ingestion.router)

@app.get("/")
async def root():
    return {"message": "RAG Chatbot Backend is running!"}
