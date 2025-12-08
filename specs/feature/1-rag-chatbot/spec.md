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