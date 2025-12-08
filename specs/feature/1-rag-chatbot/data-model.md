# Data Model for Integrated RAG Chatbot

## Entities

### 1. Conversation
-   **Description**: Represents a single chat session between the user and the chatbot.
-   **Fields**:
    -   `conversation_id` (UUID): Primary key, unique identifier for the conversation.
    -   `user_id` (String): Identifier for the user (if authenticated, otherwise anonymous).
    -   `created_at` (Timestamp): Timestamp of when the conversation started.
    -   `updated_at` (Timestamp): Timestamp of the last message in the conversation.
-   **Relationships**: One-to-many with `Message`.
-   **Storage**: Neon Postgres.

### 2. Message
-   **Description**: Represents a single message within a conversation, either from the user or the chatbot.
-   **Fields**:
    -   `message_id` (UUID): Primary key, unique identifier for the message.
    -   `conversation_id` (UUID): Foreign key, links to the parent `Conversation`.
    -   `sender` (Enum: `user`, `chatbot`): Indicates who sent the message.
    -   `content` (Text): The actual message text.
    -   `timestamp` (Timestamp): Timestamp of when the message was sent.
    -   `is_selected_text_query` (Boolean): Indicates if the message was a selected text query.
    -   `selected_text_context` (Text, Nullable): The text selected by the user, if applicable.
    -   `retrieved_chunks_metadata` (JSONB, Nullable): Metadata about the chunks retrieved for RAG, including citations.
-   **Relationships**: Many-to-one with `Conversation`.
-   **Storage**: Neon Postgres.

### 3. Document Chunk
-   **Description**: Represents a semantically meaningful portion of the source book content.
-   **Fields**:
    -   `chunk_id` (UUID/String): Unique identifier for the chunk.
    -   `content` (Text): The text content of the chunk.
    -   `embedding` (Vector): The vector embedding of the chunk content.
    -   `source_file` (String): Path to the original Markdown/MDX/TXT file.
    -   `heading` (String, Nullable): The heading under which the chunk was found.
    -   `page_number` (Integer, Nullable): Page number if applicable.
    -   `order_in_file` (Integer): Order of the chunk within its source file.
    -   `ingestion_timestamp` (Timestamp): When this chunk was ingested.
-   **Relationships**: None directly, but queried for RAG.
-   **Storage**: Qdrant Cloud (vector storage) with metadata.

### 4. Ingestion Log (Optional, but useful for debugging)
-   **Description**: Records events and status during the document ingestion pipeline.
-   **Fields**:
    -   `log_id` (UUID): Primary key.
    -   `timestamp` (Timestamp): Time of the log entry.
    -   `event_type` (String: `scan`, `chunk`, `embed`, `write_qdrant`, `error`)
    -   `file_path` (String): File being processed.
    -   `status` (String: `success`, `failure`, `in_progress`)
    -   `details` (Text, Nullable): Error messages or additional context.
-   **Storage**: Neon Postgres.

## Validation Rules

- Chatbot responses must be grounded strictly from `Document Chunk` content.
- Chunk size for ingestion: 300–500 tokens.
- `embedding` must be generated using OpenAI embeddings.
- `Message` content for user queries can be a normal text query or a selected text query.
- If a query is based on `selected_text_context`, that context is prioritized.
- If the answer is not available from the book content, the chatbot must refuse to answer with a specific message.

## State Transitions (for Conversations)

- New `Conversation` created upon first user interaction.
- `updated_at` on `Conversation` updated with each new `Message`.
- `Ingestion Log` entries transition through `in_progress`, `success`, `failure` states.