---
id: 0003
title: Create Implementation Plan for RAG Chatbot
stage: plan
date: 2025-12-07
surface: agent
model: gemini-1.5-pro-a
feature: 002-rag-chatbot
branch: 002-rag-chatbot
user: Kashaf Aman
command: /sp.plan
labels: ["plan", "rag-chatbot"]
links:
  spec: specs/002-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/002-rag-chatbot/plan.md
- specs/002-rag-chatbot/research.md
- specs/002-rag-chatbot/data-model.md
- specs/002-rag-chatbot/contracts/openapi.yaml
- specs/002-rag-chatbot/quickstart.md
tests:

---

## Prompt

/sp.plan Project: Integrated RAG Chatbot for the SpeckitPlus Book

1. Backend Setup
   - Initialize FastAPI project structure: app/, routers/, services/, db/, rag/
   - Add environment loader for OpenAI, Qdrant, Neon
   - Create health check endpoint

2. Database (Neon Postgres)
   - Define tables: conversations, messages, documents, ingestion_jobs
   - Implement async DB connection + CRUD helpers

3. Qdrant Vector Store
   - Initialize client with API key + URL
   - Create collection with embedding dimension
   - Implement upsert, search, and delete utilities

4. Ingestion Pipeline
   - Recursively scan /docs for md/mdx/txt files
   - Normalize + preprocess markdown
   - Chunk files (300–500 tokens)
   - Generate embeddings using OpenAI embeddings API
   - Store document metadata in Neon
   - Upload vectors to Qdrant
   - Connect ingestion to /ingest endpoint

5. RAG Retrieval System
   - Implement top-k semantic search
   - Add selected-text priority search
   - Combine retrieved chunks into context
   - Build grounding safety: reject ungrounded answers

6. LLM Reasoning Layer
   - Use OpenAI Agents/ChatKit for generation
   - Provide system instruction: answer ONLY from retrieved chunks
   - Add citation formatting with chunk IDs

7. API Endpoints
   - /query → RAG search + grounded answer
   - /selected-text → context-first retrieval
   - /embed → generate embeddings for text
   - /ingest → trigger full ingestion
   - /conversation → log + fetch chat history
   - /health → service heartbeat

8. Frontend Integration (Docusaurus)
   - Build JS fetch wrapper (POST query, selected-text, conversation)
   - Connect to FastAPI backend URL via env variable
   - Add UI component placeholder for chatbot widget

9. Deployment Workflow
   - Configure .env (OpenAI, Qdrant, Neon)
   - Deploy FastAPI backend (Railway, Render, or Fly.io)
   - Link Qdrant + Neon credentials
   - Test ingestion → retrieval → query end-to-end

## Response snapshot

Successfully created the implementation plan and related design artifacts for the RAG Chatbot feature. This included:
- Researching and deciding on the deployment platform and project scale.
- Defining the data model for the database.
- Creating an OpenAPI specification for the API.
- Generating a quickstart guide for developers.
- Updating the agent context with the new technologies.

## Outcome

- ✅ Impact: A comprehensive implementation plan for the RAG chatbot feature has been created.
- 🧪 Tests: None (planning phase)
- 📁 Files: 5 files created/modified.
- 🔁 Next prompts: Ready for /sp.tasks to break down the implementation into concrete tasks.
- 🧠 Reflection: The planning phase was successful, and all required artifacts were generated.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
