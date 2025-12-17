from typing import List, Optional
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Conversation, Message, Document, IngestionLog

async def create_conversation(db: AsyncSession) -> Conversation:
    conversation = Conversation()
    db.add(conversation)
    await db.commit()
    await db.refresh(conversation)
    return conversation

async def get_conversation(db: AsyncSession, conversation_id: UUID) -> Optional[Conversation]:
    result = await db.execute(select(Conversation).filter(Conversation.id == conversation_id))
    return result.scalar_one_or_none()

async def create_message(db: AsyncSession, conversation_id: UUID, role: str, content: str) -> Message:
    message = Message(conversation_id=conversation_id, role=role, content=content)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    return message

async def get_messages_for_conversation(db: AsyncSession, conversation_id: UUID) -> List[Message]:
    result = await db.execute(select(Message).filter(Message.conversation_id == conversation_id).order_by(Message.created_at))
    return result.scalars().all()

async def create_document(db: AsyncSession, source: str, content: str) -> Document:
    document = Document(source=source, content=content)
    db.add(document)
    await db.commit()
    await db.refresh(document)
    return document

async def get_documents_by_source(db: AsyncSession, source: str) -> List[Document]:
    result = await db.execute(select(Document).filter(Document.source == source))
    return result.scalars().all()

async def create_ingestion_log(db: AsyncSession, job_id: str, status: str, files_processed: int = 0) -> IngestionLog:
    ingestion_log = IngestionLog(job_id=job_id, status=status, files_processed=files_processed)
    db.add(ingestion_log)
    await db.commit()
    await db.refresh(ingestion_log)
    return ingestion_log

async def update_ingestion_log_status(db: AsyncSession, log_id: UUID, status: str, files_processed: Optional[int] = None) -> Optional[IngestionLog]:
    ingestion_log = await get_ingestion_log(db, log_id)
    if ingestion_log:
        ingestion_log.status = status
        if files_processed is not None:
            ingestion_log.files_processed = files_processed
        await db.commit()
        await db.refresh(ingestion_log)
    return ingestion_log

async def get_ingestion_log(db: AsyncSession, log_id: UUID) -> Optional[IngestionLog]:
    result = await db.execute(select(IngestionLog).filter(IngestionLog.id == log_id))
    return result.scalar_one_or_none()