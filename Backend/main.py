from fastapi import FastAPI
from app.core.config import settings
from app.routers import health, rag, ingestion

app = FastAPI()

app.include_router(health.router)
app.include_router(rag.router)
app.include_router(ingestion.router)

@app.get("/")
async def root():
    return {"message": "RAG Chatbot Backend is running!"}

