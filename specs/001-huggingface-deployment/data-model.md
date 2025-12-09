# Data Model: Hugging Face Deployment

**Date**: 2025-12-09
**Author**: Gemini

This document describes the data model for the configuration artifacts required for the Hugging Face Deployment feature. As this feature is focused on deployment, the data model primarily consists of configuration files rather than database entities.

## 1. `hf.yaml`

This file defines the metadata for the Hugging Face Space.

- **Type**: YAML
- **Location**: `my-book/hf.yaml` (or at the root of the repository if it controls the space)

### Fields

| Field      | Type   | Description                                     | Example         |
|------------|--------|-------------------------------------------------|-----------------|
| `title`    | string | The title of the Hugging Face Space.              | `My Awesome App`  |
| `emoji`    | string | An emoji to represent the Space.                | `🚀`              |
| `colorFrom`| string | The starting color of the Space's gradient.     | `blue`          |
| `colorTo`  | string | The ending color of the Space's gradient.       | `purple`        |
| `sdk`      | string | The SDK used by the Space. Must be `docker`.    | `docker`        |
| `app_file` | string | The entrypoint file for the application.        | `main.py`       |


## 2. `Dockerfile`

This file defines the Docker image for the application.

- **Type**: Dockerfile
- **Location**: Project root

### Structure

A multi-stage Dockerfile is recommended to keep the final image size small.

1.  **Stage 1: Frontend Build**
    -   Base Image: `node:18`
    -   Steps:
        -   Copy `my-book/` source code.
        -   Install Node.js dependencies (`npm install`).
        -   Build the Docusaurus application (`npm run build`).

2.  **Stage 2: Backend and Final Image**
    -   Base Image: `python:3.11-slim`
    -   Steps:
        -   Install Python dependencies from `Backend/requirements.txt`.
        -   Copy the backend source code from `Backend/`.
        -   Copy the built frontend from the `frontend-build` stage.
        -   Expose the required port (e.g., 8000).
        -   Define the `CMD` to start the FastAPI server (e.g., using `uvicorn`).

## 3. `.dockerignore`

This file specifies which files and directories to exclude from the Docker build context to improve build performance and security.

- **Type**: Plain text
- **Location**: Project root

### Content

The `.dockerignore` file should include entries for:
-   `.git`
-   `node_modules`
-   `.venv`
-   `__pycache__`
-   Any local development files or secrets.
