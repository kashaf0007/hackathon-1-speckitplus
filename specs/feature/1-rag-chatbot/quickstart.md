# Quickstart Guide: Integrated RAG Chatbot

This guide provides instructions to quickly set up, deploy, and interact with the Integrated RAG Chatbot for the SpeckitPlus Book.

## 1. Prerequisites

Before you begin, ensure you have the following installed and configured:

- **Python 3.9+** (or the recommended version after research).
- **Docker** (for containerized deployment, optional).
- **Poetry** (or pip/conda for dependency management).
- **OpenAI API Key**: Obtain one from [OpenAI](https://platform.openai.com/).
- **Qdrant Cloud Account**: Set up a Qdrant Cloud instance and obtain API key and URL.
- **Neon Postgres Account**: Set up a Neon Postgres database and obtain connection string.

## 2. Project Setup

1.  **Clone the repository** (if not already done):

    ```bash
    git clone <repository_url>
    cd speckitplus-book
    ```

2.  **Create and activate a virtual environment** (recommended with Poetry):

    ```bash
    poetry env use python3.9  # Or your preferred Python version
    poetry install
    poetry shell
    ```

    If using `pip`:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

## 3. Configuration

Create a `.env` file in the `backend/` directory with the following environment variables:

```dotenv
OPENAI_API_KEY="your_openai_api_key"
QDRANT_URL="your_qdrant_cloud_url"
QDRANT_API_KEY="your_qdrant_api_key"
NEON_POSTGRES_CONNECTION_STRING="your_neon_postgres_connection_string"
```

## 4. Ingestion Pipeline

Before querying, you need to ingest the book content into Qdrant.

1.  **Ensure `/docs` directory contains your book content** (Markdown, MDX, TXT files).
2.  **Run the ingestion script/endpoint**:

    ```bash
    # Example using a hypothetical CLI tool or direct API call
    python backend/ingest.py --docs_path /path/to/speckitplus-book/docs
    # Or via API (e.g., using curl or a client library)
    # curl -X POST -H "Content-Type: application/json" \
    #      -d '{"source_file": "/docs/chapter1.md", "chunks": [...]}' \
    #      http://localhost:8000/ingest
    ```

## 5. Running the Backend API

Navigate to the `backend/` directory and start the FastAPI application.

```bash
cd backend/
uvicorn main:app --reload
```

The API will be accessible at `http://localhost:8000`.

## 6. Frontend Integration (Docusaurus)

To integrate the chatbot into your Docusaurus book:

1.  **Include the provided JavaScript fetch wrapper** (e.g., `frontend/src/services/chatbot-api.js`) in your Docusaurus project.
2.  **Embed the chatbot widget/UI** (e.g., `frontend/src/components/ChatbotWidget.jsx`) into your Docusaurus theme or specific pages.

    Example Docusaurus component integration:

    ```jsx
    // pages/index.js
    import React from 'react';
    import Layout from '@theme/Layout';
    import ChatbotWidget from '@site/src/components/ChatbotWidget';

    function HomePage() {
      return (
        <Layout title="Home" description="SpeckitPlus Book with RAG Chatbot">
          <div>
            <h1>Welcome to the SpeckitPlus Book</h1>
            {/* Other content */}
            <ChatbotWidget />
          </div>
        </Layout>
      );
    }

    export default HomePage;
    ```

## 7. Testing

After setting up, perform basic tests:

1.  **Ingestion Test**: Ensure `/docs` content is successfully ingested (check Qdrant console).
2.  **Query Test**: Send a query to `/query` endpoint and verify a grounded answer with citations.
3.  **Selected Text Query Test**: Test `/selected-text` endpoint with a portion of the book content.
4.  **Conversation Test**: Verify conversation history retrieval from Neon Postgres via `/conversation`.

## 8. Deployment (Production)

For production deployment, consider:

-   Using a robust ASGI server like Gunicorn with Uvicorn workers.
-   Containerization with Docker.
-   Orchestration with Kubernetes or a PaaS like Render, Heroku, or AWS App Runner.
-   Setting up CI/CD pipelines.
-   Monitoring and logging solutions.

**Note**: Replace placeholder values like `<repository_url>`, `your_openai_api_key`, etc., with actual credentials and paths.