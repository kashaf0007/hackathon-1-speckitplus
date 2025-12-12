# SpecKitPlus Book

This repository contains the source code for the SpecKitPlus Book, a documentation website built with Docusaurus, and a RAG (Retrieval-Augmented Generation) chatbot backend built with FastAPI and Authentication with Better-auth .

## Project Structure

- `my-book/`: The Docusaurus frontend for the documentation website.
- `Backend/`: The FastAPI backend for the RAG chatbot.
- `specs/`: The specifications and design documents for the project features.

## Basic Setup

### Frontend

1.  Navigate to the `my-book/` directory.
2.  Install dependencies: `npm install`
3.  Start the development server: `npm start`

### Backend

1.  Navigate to the `Backend/` directory.
2.  Create a virtual environment: `python -m venv .venv`
3.  Activate the virtual environment.
4.  Install dependencies: `pip install -r requirements.txt`
5.  Start the development server: `uvicorn main:app --reload`

## Hugging Face Deployment

This project is configured for deployment to Hugging Face Spaces using Docker.

### Deployment Steps

1.  **Create a new Space on Hugging Face**:
    -   Go to [huggingface.co/new-space](https://huggingface.co/new-space).
    -   Select "Docker" as the Space SDK.
    -   Choose a name for your Space.
    -   Select "Public" or "Private" visibility.
    -   Click "Create Space".

2.  **Push the code to the Space**:
    -   Follow the instructions on the Hugging Face Space page to clone the repository, add your code, and push the changes.

    ```bash
    git clone https://huggingface.co/spaces/<your-username>/<your-space-name>
    cd <your-space-name>
    # Add your project files
    git add .
    git commit -m "Initial commit"
    git push
    ```

3.  **Monitor the build**:
    -   The Space will automatically start building after you push your code.
    -   You can monitor the build logs on the Space's page.

4.  **Access the application**:
    -   Once the build is complete, your application will be available at `https://<your-username>-<your-space-name>.hf.space`.

### Usage Examples

The deployed application will have two main parts:

-   **The Docusaurus documentation website**: Accessible at the root URL of the Space.
-   **The FastAPI backend**: The API endpoints will be available under the `/api` path. For example, `https://<your-username>-<your-space-name>.hf.space/api/health`.
