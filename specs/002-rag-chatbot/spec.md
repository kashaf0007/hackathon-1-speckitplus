# Feature Specification: RAG Chatbot

**Feature Branch**: `002-rag-chatbot`  
**Created**: 2025-12-07
**Status**: Draft  
**Input**: User description: "1. Requirements Understanding - Read all /docs content. - Confirm chatbot must answer strictly from book content. - Support both normal queries and selected-text queries. 2. System Architecture - FastAPI backend. - OpenAI Agents/ChatKit for LLM orchestration. - Qdrant Cloud for vector search. - Neon Postgres for conversations, messages, ingestion logs. 3. Ingestion Pipeline - Recursively scan /docs. - Chunk md/mdx/txt files (300–500 tokens). - Generate embeddings. - Write data to Qdrant with metadata. 4. RAG Query Flow - Normal query: vector search → retrieve chunks → generate grounded answer. - Selected text: prioritize selected context → fallback to global. - Enforce “only from book” rule; refuse unsupported answers. 5. API Development - Endpoints: /query, /embed, /ingest, /selected-text, /conversation, /health. - Logging to Neon DB. - Add middleware for API key/auth. 6. Frontend Integration - Provide simple fetch wrapper for Docusaurus. - Embed chatbot widget/UI in book. 7. Deployment - Set environment variables (.env). - Deploy FastAPI backend. - Connect to Neon DB + Qdrant Cloud. - Test ingestion → retrieval → query flow. 8. QA & Validation - Test with multiple chapters. - Validate no hallucinations. - Validate chunk citations."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Query the book for information (Priority: P1)

As a user, I want to ask a question in the chatbot and get a relevant answer based on the content of the book, so that I can quickly find the information I need.

**Why this priority**: This is the core functionality of the chatbot.

**Independent Test**: Can be tested by asking a question and verifying that the answer is relevant and accurate based on the book's content.

**Acceptance Scenarios**:

1. **Given** the chatbot is open, **When** I type a question and press enter, **Then** I should see an answer that is relevant to my question and derived from the book's content.
2. **Given** I have asked a question, **When** the chatbot provides an answer, **Then** the answer should cite the sources from the book that were used to generate it.

---

### User Story 2 - Ask a question about selected text (Priority: P2)

As a user, I want to highlight a section of the book's text and ask a question about it, so that I can get a specific answer based on the context I provide.

**Why this priority**: This provides a more focused and contextual way of interacting with the chatbot.

**Independent Test**: Can be tested by selecting a piece of text, asking a question, and verifying the answer is based on the selected text.

**Acceptance Scenarios**:

1. **Given** I have selected a piece of text in the book, **When** I ask a question to the chatbot, **Then** the answer should be primarily based on the selected text.
2. **Given** I have asked a question about a selected text, **When** the answer cannot be found in the selected text, **Then** the chatbot should search the rest of the book for an answer.

---

### User Story 3 - Content Ingestion (Priority: P3)

As an administrator, I want the chatbot to automatically index the content of the book, so that the chatbot is always up-to-date with the latest changes.

**Why this priority**: This is essential for maintaining the chatbot's knowledge base.

**Independent Test**: Can be tested by adding a new document to the book and verifying that the chatbot can answer questions about it.

**Acceptance Scenarios**:

1. **Given** new content is added to the `/docs` directory, **When** the ingestion process runs, **Then** the new content should be searchable by the chatbot.

---

### Edge Cases

- What happens when a user asks a question that is not related to the book? The chatbot should politely refuse to answer.
- How does the system handle very long user queries? The maximum query length should be 500 characters. If a query exceeds this limit, the system should truncate it and inform the user.
- How does the system handle different file formats in the `/docs` directory? It should only process `md`, `mdx`, and `txt` files.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a chatbot interface embedded in the Docusaurus book.
- **FR-002**: System MUST answer user queries based solely on the content of the book.
- **FR-003**: System MUST support both general queries and queries about user-selected text.
- **FR-004**: System MUST refuse to answer questions that are not related to the book's content.
- **FR-005**: System MUST automatically scan and index new content from the `/docs` directory.
- **FR-006**: System MUST only index files with `.md`, `.mdx`, and `.txt` extensions.
- **FR-007**: System MUST log all conversations and ingestion events.
- **FR-008**: System MUST provide citations for the sources used to generate an answer.
- **FR-009**: The chatbot's API endpoints MUST be protected using an API Key.

### Key Entities *(include if feature involves data)*

- **Conversation**: Represents a user's interaction with the chatbot, containing one or more messages.
- **Message**: A single query from a user or a response from the chatbot.
- **Document**: A chunk of text from the book's content that is indexed and used for retrieval.
- **IngestionLog**: A record of a content ingestion event, including the files that were processed.

## Assumptions

- The Docusaurus book content is primarily Markdown (`.md`, `.mdx`) and plain text (`.txt`).
- The chatbot will be integrated into the Docusaurus frontend as a widget or similar UI element.
- The external services (Qdrant, Neon Postgres, OpenAI) are available and configured.
- The FastAPI backend can be deployed and scaled as needed.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of user queries should receive a relevant answer in under 5 seconds.
- **SC-002**: The chatbot should successfully refuse to answer more than 99% of out-of-scope questions.
- **SC-003**: New content should be searchable by the chatbot within 5 minutes of being added to the `/docs` directory.
- **SC-004**: The chatbot's answers should be grounded in the book's content, with no hallucinations, in 99% of cases.