import os
from typing import List
import markdown # Import markdown library
import re
from app.rag.retrieval import generate_embedding # Import generate_embedding
from app.db.session import create_document # Import create_document
from sqlalchemy.ext.asyncio import AsyncSession # Import AsyncSession
from app.rag.qdrant import upsert_vectors # Import upsert_vectors
import uuid # Import uuid for generating point IDs

def get_document_paths(docs_dir: str) -> List[str]:
    document_paths = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith((".md", ".mdx", ".txt")):
                document_paths.append(os.path.join(root, file))
    return document_paths

def read_document_content(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def preprocess_markdown(markdown_content: str) -> str:
    # Convert markdown to plain text
    html = markdown.markdown(markdown_content)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def chunk_text(text: str, chunk_size: int = 1500, overlap: int = 100) -> List[str]:
    """
    Splits text into chunks of specified size with overlap.
    Aims for ~300-500 tokens, which is ~1200-2000 characters.
    """
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end > len(text):
            chunks.append(text[start:])
            break
        
        # Try to find a natural break point (e.g., end of a sentence or paragraph)
        # within the overlap or slightly before the end of the chunk
        break_point = text.rfind('.', start, end)
        if break_point == -1: # No sentence end found
            break_point = text.rfind('\n', start, end)
        if break_point == -1: # No paragraph end found
            break_point = end # Fallback to hard cut

        chunks.append(text[start:break_point].strip())
        start = break_point - overlap if break_point - overlap > start else break_point

    return [chunk for chunk in chunks if chunk]

async def ingest_documents(db: AsyncSession, docs_dir: str = "my-book/docs"):
    print(f"Starting ingestion from {docs_dir}...")
    document_paths = get_document_paths(docs_dir)
    print(f"Found {len(document_paths)} documents.")
    
    for doc_path in document_paths:
        content = read_document_content(doc_path)
        
        # Preprocess markdown content
        if doc_path.endswith((".md", ".mdx")):
            processed_content = preprocess_markdown(content)
        else: # .txt files
            processed_content = content
            
        print(f"Processing {doc_path} (original length: {len(content)}, processed length: {len(processed_content)})...")
        
        chunks = chunk_text(processed_content)
        print(f"Generated {len(chunks)} chunks for {doc_path}.")
        
        vectors = []
        payloads = []
        point_ids = []

        for i, chunk in enumerate(chunks):
            # Store document metadata in Neon Postgres
            document = await create_document(db, source=doc_path, content=chunk)
            embedding = await generate_embedding(chunk)
            print(f"Generated embedding for chunk {i+1}/{len(chunks)} of {doc_path}. Document ID: {document.id}")
            
            vectors.append(embedding)
            payloads.append({
                "source": doc_path,
                "content": chunk,
                "document_id": str(document.id)
            })
            point_ids.append(str(document.id))

        if vectors:
            await upsert_vectors(vectors=vectors, payloads=payloads)
            print(f"Uploaded {len(vectors)} vectors to Qdrant for {doc_path}.")
    
    print("Ingestion process completed.")

if __name__ == "__main__":
    import asyncio
    # This part needs to be updated to provide a DB session if run directly
    # For now, it will not run correctly without a session
    print("This script is intended to be run via the FastAPI endpoint or with a proper DB session.")