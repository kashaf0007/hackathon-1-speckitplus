---
id: 1
title: Integrated RAG Chatbot for SpeckitPlus Book
stage: constitution
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20251101
feature: none
branch: main
user: user
command: /sp.contitution create "Integrated RAG Chatbot for SpeckitPlus Book" 1. Data Source:
   - Chatbot answers ONLY from /docs.
   - Use chunked retrieval with Qdrant; cite retrieved chunks.

2. RAG Pipeline:
   - Use OpenAI Agents/ChatKit.
   - Backend: FastAPI with endpoints /query, /embed, /ingest, /selected-text, /conversation.
   - Storage: Neon Postgres.
   - Vectors: Qdrant Cloud.

3. Ingestion:
   - Scan /docs for md/mdx/txt.
   - Chunk 300–500 tokens.
   - Embed with OpenAI; store metadata (file, heading, chunk_id, text).

4. Query Rules:
   - Normal query → vector search → answer from top-k chunks only.
   - Selected text → prioritize its context; fallback to global.
   - If unsupported → respond: “Not available in the SpeckitPlus Book.”

5. Behavior:
   - No hallucinations; maintain teaching tone.

6. Deployment:
   - Backend callable from Docusaurus.
   - Provide JS fetch wrapper.
   - Log all actions to Neon DB.
labels: [constitution]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
null
---

## Prompt

/sp.contitution create "Integrated RAG Chatbot for SpeckitPlus Book" 1. Data Source:
   - Chatbot answers ONLY from /docs.
   - Use chunked retrieval with Qdrant; cite retrieved chunks.

2. RAG Pipeline:
   - Use OpenAI Agents/ChatKit.
   - Backend: FastAPI with endpoints /query, /embed, /ingest, /selected-text, /conversation.
   - Storage: Neon Postgres.
   - Vectors: Qdrant Cloud.

3. Ingestion:
   - Scan /docs for md/mdx/txt.
   - Chunk 300–500 tokens.
   - Embed with OpenAI; store metadata (file, heading, chunk_id, text).

4. Query Rules:
   - Normal query → vector search → answer from top-k chunks only.
   - Selected text → prioritize its context; fallback to global.
   - If unsupported → respond: “Not available in the SpeckitPlus Book.”

5. Behavior:
   - No hallucinations; maintain teaching tone.

6. Deployment:
   - Backend callable from Docusaurus.
   - Provide JS fetch wrapper.
   - Log all actions to Neon DB.

## Response snapshot

Created or updated the project constitution with the provided principles.

## Outcome

- ✅ Impact: Constitution updated.
- 🧪 Tests: N/A
- 📁 Files: 1 file modified
- 🔁 Next prompts: N/A
- 🧠 Reflection: Updated project constitution based on user input for RAG Chatbot.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
