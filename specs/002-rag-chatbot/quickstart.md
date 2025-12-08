# Quickstart

This document provides a quick overview of how to get started with the RAG chatbot feature.

## Backend

1.  **Install dependencies**: `pip install -r requirements.txt`
2.  **Set environment variables**: Create a `.env` file with the following variables:
    ```
    OPENAI_API_KEY=...
    QDRANT_API_KEY=...
    QDRANT_URL=...
    NEON_DATABASE_URL=...
    ```
3.  **Run the application**: `uvicorn main:app --reload`
4.  **Trigger ingestion**: Send a POST request to `http://localhost:8000/ingest` to start the document ingestion process.

## Frontend

1.  **Install dependencies**: `npm install`
2.  **Run the application**: `npm start`
3.  The chatbot widget will be available on the book's pages.

## API Usage

-   **Query**: Send a POST request to `http://localhost:8000/query` with a JSON body containing the `query` and `conversation_id`.
-   **Selected Text Query**: Send a POST request to `http://localhost:8000/selected-text` with a JSON body containing the `query`, `text`, and `conversation_id`.
-   **Get Conversation**: Send a GET request to `http://localhost:8000/conversation?conversation_id=...` to get the conversation history.
