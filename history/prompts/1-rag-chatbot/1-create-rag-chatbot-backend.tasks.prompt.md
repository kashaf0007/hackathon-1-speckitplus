---
id: 1
title: Create RAG Chatbot Backend Structure and Functionality
stage: tasks
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20251101
feature: 1-rag-chatbot
branch: feature/1-rag-chatbot
user: null
command: "/sp.task 1. Create FastAPI backend structure (app/, routers/, services/, db/, rag/). 2. Add .env loader and environment variable validation. 3. Implement Neon Postgres connection (async). 4. Implement Qdrant client + collection setup. 5. Build ingestion script: - Read /docs - Chunk files - Generate embeddings - Upload vectors to Qdrant 6. Implement /ingest endpoint to trigger ingestion. 7. Implement RAG retrieval: - Vector search (top-k) - Selected-text priority retrieval 8. Implement ChatKit/OpenAI agent for grounded answers. 9. Build /query and /selected-text endpoints. 10. Store conversations + messages in Neon DB. 11. Create JS fetch wrapper for Docusaurus frontend. 12. Deploy backend and connect Qdrant + Neon. 13. Test RAG flow end-to-end."
labels: ["rag-chatbot", "backend", "fastapi", "qdrant", "neon-postgres", "ingestion", "api-endpoints"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  -
tests:
  -
---

## Prompt

/sp.task 1. Create FastAPI backend structure (app/, routers/, services/, db/, rag/).
2. Add .env loader and environment variable validation.
3. Implement Neon Postgres connection (async).
4. Implement Qdrant client + collection setup.
5. Build ingestion script:
   - Read /docs
   - Chunk files
   - Generate embeddings
   - Upload vectors to Qdrant
6. Implement /ingest endpoint to trigger ingestion.
7. Implement RAG retrieval:
   - Vector search (top-k)
   - Selected-text priority retrieval
8. Implement ChatKit/OpenAI agent for grounded answers.
9. Build /query and /selected-text endpoints.
10. Store conversations + messages in Neon DB.
11. Create JS fetch wrapper for Docusaurus frontend.
12. Deploy backend and connect Qdrant + Neon.
13. Test RAG flow end-to-end.

## Response snapshot

null

## Outcome

- ✅ Impact: null
- 🧪 Tests: null
- 📁 Files: null
- 🔁 Next prompts: null
- 🧠 Reflection: null

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
