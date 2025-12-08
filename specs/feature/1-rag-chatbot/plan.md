# Implementation Plan: Integrated RAG Chatbot for the SpeckitPlus Book

**Branch**: `feature/1-rag-chatbot` | **Date**: 2025-12-07 | **Spec**: /specs/feature/1-rag-chatbot/spec.md
**Input**: Feature specification from `/specs/1-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement an integrated RAG Chatbot for the SpeckitPlus Book, featuring a FastAPI backend for ingestion and querying, utilizing Neon Postgres for metadata and Qdrant for vector storage, and an OpenAI LLM reasoning layer. The system will support both normal and selected-text queries, with a focus on grounding answers strictly from book content, and integrate with Docusaurus for frontend presentation.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: FastAPI, OpenAI, Qdrant-client, psycopg2-binary (for Neon Postgres)
**Storage**: Neon PostgreSQL, Qdrant Cloud
**Testing**: pytest (NEEDS CLARIFICATION: Specific testing frameworks or libraries?)
**Target Platform**: Linux server (for FastAPI backend), Web (for Docusaurus frontend)
**Project Type**: Web application (backend + frontend)
**Performance Goals**: NEEDS CLARIFICATION: Specific latency or throughput targets for API endpoints?
**Constraints**: Answer ONLY from retrieved book content.
**Scale/Scope**: Intended for the SpeckitPlus Book content. NEEDS CLARIFICATION: Expected number of users or query volume?

**Backend Setup**:
- Initialize FastAPI project structure: `app/`, `routers/`, `services/`, `db/`, `rag/`
- Environment loader for OpenAI, Qdrant, Neon (Convention: Use `OPENAI_API_KEY`, `QDRANT_URL`, `NEON_DATABASE_URL` for convenience and `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` for granular control, managed by Pydantic\'s BaseSettings.)
- Health check endpoint

**Database (Neon Postgres)**:
- Define tables: `conversations`, `messages`, `documents`, `ingestion_jobs`
- Implement async DB connection + CRUD helpers (ORM: SQLAlchemy 2.0 with asyncpg driver.)

**Qdrant Vector Store**:
- Initialize client with API key + URL
- Create collection with embedding dimension (Embedding model: `text-embedding-3-small` (default 1536 dimensions). Dimension size: 1536. Distance metric: COSINE.)
- Implement upsert, search, and delete utilities

**Ingestion Pipeline**:
- Recursively scan `/docs` for `md`/`mdx`/`txt` files
- Normalize + preprocess markdown (NEEDS CLARIFICATION: Specific normalization steps (e.g., stripping front matter, converting to plain text, handling code blocks)? Preprocessing steps (e.g., cleaning special characters)?)
- Chunk files (300–500 tokens) (NEEDS CLARIFICATION: Chunking strategy (e.g., recursive character text splitter)? Overlap size between chunks (e.g., 50-100 tokens)?)
- Generate embeddings using OpenAI embeddings API
- Store document metadata in Neon
- Upload vectors to Qdrant
- Connect ingestion to `/ingest` endpoint

**RAG Retrieval System**:
- Top-k semantic search (NEEDS CLARIFICATION: Value of `k` (e.g., 3-5 chunks)? How to handle multiple retrieved chunks (e.g., concatenate, summarize before passing to LLM)?)
- Selected-text priority search (NEEDS CLARIFICATION: How is "selected-text priority" implemented (e.g., direct vector search on selected text, or using selected text to re-rank initial results)? How does it interact with top-k?)
- Combine retrieved chunks into context (NEEDS CLARIFICATION: Concatenation strategy? Max context window for LLM?)
- Build grounding safety: reject ungrounded answers (NEEDS CLARIFICATION: Specific grounding safety mechanism (e.g., confidence scoring, separate LLM call to verify grounding)? Confidence threshold?)

**LLM Reasoning Layer**:
- Use OpenAI Agents/ChatKit for generation (NEEDS CLARIFICATION: Specific OpenAI model? (e.g., `gpt-3.5-turbo`, `gpt-4-turbo`))
- Provide system instruction: answer ONLY from retrieved chunks
- Add citation formatting with chunk IDs

**API Endpoints**:
- `/query` → RAG search + grounded answer
- `/selected-text` → context-first retrieval
- `/embed` → generate embeddings for text
- `/ingest` → trigger full ingestion
- `/conversation` → log + fetch chat history
- `/health` → service heartbeat

**Frontend Integration (Docusaurus)**:
- Build JS fetch wrapper (`POST` query, `selected-text`, `conversation`)
- Connect to FastAPI backend URL via env variable
- UI component placeholder for chatbot widget (NEEDS CLARIFICATION: Specific Docusaurus integration points (e.g., custom plugin, theme component override)?)

**Deployment Workflow**:
- Configure `.env` (OpenAI, Qdrant, Neon)
- Deploy FastAPI backend (NEEDS CLARIFICATION: Preferred deployment platform? (Railway, Render, or Fly.io))
- Link Qdrant + Neon credentials
- Test ingestion → retrieval → query end-to-end

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The `constitution.md` file is currently in a template state. A proper constitution needs to be defined to perform a meaningful check against core principles and gates. This section currently reflects the template placeholders.

## Project Structure

### Documentation (this feature)

```text
specs/1-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── routers/
│   ├── services/
│   ├── db/
│   └── rag/
├── tests/
└── main.py
├── ingest.py
└── requirements.txt

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/
```

**Structure Decision**: The project will follow a monorepo-like structure with distinct `backend/` and `frontend/` directories at the repository root, as per "Option 2: Web application" from the template, adapted to the FastAPI and Docusaurus components.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations detected as the constitution itself is a template.