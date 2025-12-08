from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.connection import get_db
from app.db import session as db_session
from app.rag.retrieval import generate_embedding, retrieve_context
from app.rag.agent import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    conversation_id: Optional[UUID] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[str]
    conversation_id: UUID

class SelectedTextQueryRequest(BaseModel):
    query: str
    text: str
    conversation_id: Optional[UUID] = None

class EmbedRequest(BaseModel):
    text: str

class EmbedResponse(BaseModel):
    embedding: List[float]

@router.post("/query", response_model=QueryResponse)
async def query_chatbot(request: QueryRequest, db: AsyncSession = Depends(get_db)):
    if request.conversation_id:
        conversation = await db_session.get_conversation(db, request.conversation_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        conversation = await db_session.create_conversation(db)

    # Store user message
    await db_session.create_message(db, conversation.id, "user", request.query)

    # Retrieve context
    context_with_sources = await retrieve_context(request.query)
    context_content = [item["content"] for item in context_with_sources]
    sources = [item["source"] for item in context_with_sources]

    # Generate answer
    answer = await generate_answer(request.query, context_content)

    # Store assistant message
    await db_session.create_message(db, conversation.id, "assistant", answer)

    return QueryResponse(answer=answer, sources=sources, conversation_id=conversation.id)

@router.post("/selected-text", response_model=QueryResponse)
async def query_selected_text_chatbot(request: SelectedTextQueryRequest, db: AsyncSession = Depends(get_db)):
    if request.conversation_id:
        conversation = await db_session.get_conversation(db, request.conversation_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        conversation = await db_session.create_conversation(db)

    # Store user message
    await db_session.create_message(db, conversation.id, "user", request.query)

    # Retrieve context with selected text priority
    context_with_sources = await retrieve_context(request.query, request.text)
    context_content = [item["content"] for item in context_with_sources]
    sources = [item["source"] for item in context_with_sources]

    # Generate answer
    answer = await generate_answer(request.query, context_content)

    # Store assistant message
    await db_session.create_message(db, conversation.id, "assistant", answer)

    return QueryResponse(answer=answer, sources=sources, conversation_id=conversation.id)

@router.post("/embed", response_model=EmbedResponse)
async def embed_text(request: EmbedRequest):
    embedding = await generate_embedding(request.text)
    return EmbedResponse(embedding=embedding)

class MessageResponse(BaseModel):
    role: str
    content: str

@router.get("/conversation/{conversation_id}", response_model=List[MessageResponse])
async def get_conversation_history(conversation_id: UUID, db: AsyncSession = Depends(get_db)):
    messages = await db_session.get_messages_for_conversation(db, conversation_id)
    if not messages:
        raise HTTPException(status_code=404, detail="Conversation not found or no messages")
    return [MessageResponse(role=msg.role, content=msg.content) for msg in messages]