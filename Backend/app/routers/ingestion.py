from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.connection import get_db
from app.db import session as db_session
from app.ingest import ingest_documents
from app.core.security import get_api_key

router = APIRouter()

@router.post("/ingest", status_code=202, dependencies=[Depends(get_api_key)])
async def trigger_ingestion(background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    job_id = "ingestion_job_" + db_session.uuid.uuid4().hex # Generate a job ID
    ingestion_log = await db_session.create_ingestion_log(db, job_id=job_id, status="pending")
    
    background_tasks.add_task(ingest_documents_with_log, db, ingestion_log.id)
    
    return {"message": "Ingestion process started in background", "job_id": job_id}

async def ingest_documents_with_log(db: AsyncSession, log_id: db_session.UUID):
    try:
        await db_session.update_ingestion_log_status(db, log_id, "running")
        await ingest_documents(db)
        await db_session.update_ingestion_log_status(db, log_id, "completed")
    except Exception as e:
        print(f"Ingestion failed: {e}")
        await db_session.update_ingestion_log_status(db, log_id, "failed")