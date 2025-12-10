# Tasks: Integrated RAG Chatbot

**Input**: Design documents from `specs/002-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create FastAPI project structure in `backend/app/` (`core/`, `db/`, `rag/`, `routers/`, `services/`)
- [X] T002 Initialize Python project with FastAPI dependencies in `backend/requirements.txt`
- [X] T003 [P] Add environment loader for OpenAI, Qdrant, Neon in `backend/app/core/config.py`
- [X] T004 Create health check endpoint in `backend/app/routers/health.py` and register it in `backend/main.py`
- [X] T005 [P] Configure linting and formatting tools (e.g., `ruff`, `black`) for the `backend/` directory

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Setup Neon Postgres database connection in `backend/app/db/connection.py`
- [X] T007 Define tables for `Conversation`, `Message`, `Document`, `IngestionLog` in `backend/app/db/models.py`
- [X] T008 Implement async DB CRUD helpers in `backend/app/db/session.py`
- [X] T009 Initialize Qdrant client with API key + URL in `backend/app/rag/qdrant.py`
- [X] T010 Create Qdrant collection with embedding dimension in `backend/app/rag/qdrant.py`
- [X] T011 Implement Qdrant upsert, search, and delete utilities in `backend/app/rag/qdrant.py`
- [X] T012 Implement API Key authentication middleware for FastAPI in `backend/app/core/security.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Query the book for information (Priority: P1) 🎯 MVP

**Goal**: Enable users to ask general questions and receive grounded answers from the book content.

**Independent Test**: Ask a question in the chatbot and verify a relevant, accurate, and cited answer is returned based on the book's content.

### Implementation for User Story 1

- [X] T013 [P] [US1] Implement top-k semantic search in `backend/app/rag/retrieval.py`
- [X] T014 [US1] Build grounding safety mechanism (reject ungrounded answers) in `backend/app/rag/agent.py`
- [X] T015 [US1] Integrate OpenAI Agents/ChatKit for generation with system instruction ("answer ONLY from retrieved chunks") in `backend/app/rag/agent.py`
- [X] T016 [P] [US1] Add citation formatting with chunk IDs in `backend/app/rag/agent.py`
- [X] T017 [US1] Create `/query` API endpoint in `backend/app/routers/rag.py` that utilizes retrieval and LLM agent.
- [X] T018 [US1] Implement basic JS fetch wrapper for `/query` in `my-book/src/services/chatbot.js`
- [X] T019 [US1] Create a simple popup chat widget for a RAG chatbot in `my-book/src/components/ChatbotWidget/index.tsx`
- [X] T020 [US1] Embed chatbot widget into Docusaurus book (e.g., a common layout or sidebar)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Ask a question about selected text (Priority: P2)

**Goal**: Allow users to highlight text and ask questions relevant to that specific context.

**Independent Test**: Select a piece of text, ask a question, and verify the answer is based primarily on the selected text, falling back to the global context if needed.

### Implementation for User Story 2

- [X] T021 [P] [US2] Extend RAG Retrieval System for selected-text priority search in `backend/app/rag/retrieval.py`
- [X] T022 [US2] Create `/selected-text` API endpoint in `backend/app/routers/rag.py`
- [X] T023 [US2] Extend JS fetch wrapper in `my-book/src/services/chatbot.js` for `/selected-text`
- [X] T024 [US2] Extend Docusaurus frontend integration for selected-text queries (e.g., context menu integration)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Content Ingestion (Priority: P3)

**Goal**: Automatically index new book content, keeping the chatbot's knowledge base up-to-date.

**Independent Test**: Add a new document to the `/docs` directory and verify that the chatbot can answer questions about its content after ingestion.

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement recursive scan of `/docs` for `md`/`mdx`/`txt` files in `backend/ingest.py`
- [X] T026 [P] [US3] Implement normalization and preprocessing for markdown files in `backend/ingest.py`
- [X] T027 [P] [US3] Implement chunking files (300–500 tokens) in `backend/ingest.py`
- [X] T028 [P] [US3] Integrate OpenAI embeddings API for generating embeddings in `backend/ingest.py`
- [X] T029 [US3] Store document metadata in Neon Postgres in `backend/ingest.py` (using `backend/app/db/session.py`)
- [X] T030 [US3] Upload vectors to Qdrant in `backend/ingest.py` (using `backend/app/rag/qdrant.py`)
- [X] T031 [US3] Create `/ingest` API endpoint in `backend/app/routers/ingestion.py` to trigger the full ingestion process.

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T032 [P] Implement `/embed` API endpoint in `backend/app/routers/rag.py`
- [X] T033 [US1, US2] Implement logging of conversations and messages to Neon Postgres in `backend/app/db/session.py`
- [X] T034 [P] Implement `/conversation` API endpoint (log + fetch chat history) in `backend/app/routers/rag.py`
- [X] T035 Run `quickstart.md` validation, ensuring all steps are accurate and functional.
- [X] T036 Code cleanup and refactoring across the backend and frontend.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
