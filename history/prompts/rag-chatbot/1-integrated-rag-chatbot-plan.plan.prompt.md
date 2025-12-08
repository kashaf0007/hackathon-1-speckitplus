---
id: 1
title: Integrated RAG Chatbot Plan
stage: plan
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: 1-rag-chatbot
branch: feature/1-rag-chatbot
user: Kashaf Aman
command: /sp.plan
labels: [rag, chatbot, planning]
links:
  spec: specs/feature/1-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/feature/1-rag-chatbot/plan.md
  - specs/feature/1-rag-chatbot/research.md
  - specs/feature/1-rag-chatbot/data-model.md
  - specs/feature/1-rag-chatbot/contracts/query_api.yaml
  - specs/feature/1-rag-chatbot/contracts/ingestion_api.yaml
  - specs/feature/1-rag-chatbot/contracts/conversation_api.yaml
  - specs/feature/1-rag-chatbot/quickstart.md
tests:
null
---

## Prompt

```text
1. Requirements Understanding
   - Read all /docs content.
   - Confirm chatbot must answer strictly from book content.
   - Support both normal queries and selected-text queries.

2. System Architecture
   - FastAPI backend.
   - OpenAI Agents/ChatKit for LLM orchestration.
   - Qdrant Cloud for vector search.
   - Neon Postgres for conversations, messages, ingestion logs.

3. Ingestion Pipeline
   - Recursively scan /docs.
   - Chunk md/mdx/txt files (300–500 tokens).
   - Generate embeddings.
   - Write data to Qdrant with metadata.

4. RAG Query Flow
   - Normal query: vector search → retrieve chunks → generate grounded answer.
   - Selected text: prioritize selected context → fallback to global.
   - Enforce “only from book” rule; refuse unsupported answers.

5. API Development
   - Endpoints: /query, /embed, /ingest, /selected-text, /conversation, /health.
   - Logging to Neon DB.
   - Add middleware for API key/auth.

6. Frontend Integration
   - Provide simple fetch wrapper for Docusaurus.
   - Embed chatbot widget/UI in book.

7. Deployment
   - Set environment variables (.env).
   - Deploy FastAPI backend.
   - Connect to Neon DB + Qdrant Cloud.
   - Test ingestion → retrieval → query flow.

8. QA & Validation
   - Test with multiple chapters.
   - Validate no hallucinations.
   - Validate chunk citations.
```

## Response snapshot

The `/sp.plan` command executed the planning workflow, generating several design artifacts for the Integrated RAG Chatbot feature. This included updating `plan.md` with technical context, a constitution check, and project structure decisions. Research was conducted (partially blocked by tool access) and summarized in `research.md`. A detailed `data-model.md` was created, along with OpenAPI specifications for query, ingestion, and conversation APIs in the `contracts/` directory. Finally, a `quickstart.md` guide was generated.

## Outcome

- ✅ Impact: The /sp.plan command successfully generated a comprehensive set of planning artifacts for the RAG Chatbot feature.
- 🧪 Tests: Not applicable for planning phase.
- 📁 Files: `plan.md`, `research.md`, `data-model.md`, `contracts/query_api.yaml`, `contracts/ingestion_api.yaml`, `contracts/conversation_api.yaml`, `quickstart.md`, and `CLAUDE.md` (agent context update).
- 🔁 Next prompts: Suggest `/sp.adr "RAG Chatbot Architecture Decisions"`
- 🧠 Reflection: Encountered repeated tool access denials for `WebSearch` which impacted the completeness of `research.md`. Manual PHR creation was necessary due to script execution issues.

## Evaluation notes (flywheel)

- Failure modes observed: `WebSearch` tool access denied, `bash.exe` script execution errors.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Investigate `WebSearch` tool access for subsequent research tasks and improve robustness of script execution for PHR creation.