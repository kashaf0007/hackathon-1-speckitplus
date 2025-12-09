# Quickstart: Hugging Face Deployment

**Date**: 2025-12-09
**Author**: Gemini

This guide provides a quick overview of how to deploy the project to Hugging Face Spaces.

## Prerequisites

- A Hugging Face account.
- Git installed and configured.
- You have been added as a contributor to the project's repository on Hugging Face.

## Deployment Steps

1.  **Create a Dockerfile**:
    -   Create a `Dockerfile` in the root of the project with the content specified in the `data-model.md`.

2.  **Create `hf.yaml`**:
    -   Create an `hf.yaml` file in the `my-book` directory with the content specified in the `data-model.md`.

3.  **Create a new Space on Hugging Face**:
    -   Go to [huggingface.co/new-space](https://huggingface.co/new-space).
    -   Select "Docker" as the Space SDK.
    -   Choose a name for your Space.
    -   Select "Public" or "Private" visibility.
    -   Click "Create Space".

4.  **Push the code to the Space**:
    -   Follow the instructions on the Hugging Face Space page to clone the repository, add your code, and push the changes.

    ```bash
    git clone https://huggingface.co/spaces/<your-username>/<your-space-name>
    cd <your-space-name>
    # Add your project files
    git add .
    git commit -m "Initial commit"
    git push
    ```

5.  **Monitor the build**:
    -   The Space will automatically start building after you push your code.
    -   You can monitor the build logs on the Space's page.

6.  **Access the application**:
    -   Once the build is complete, your application will be available at `https://<your-username>-<your-space-name>.hf.space`.

## Local Development

To run the application locally using Docker, you can use the following commands:

```bash
# Build the Docker image
docker build -t my-app .

# Run the Docker container
docker run -p 8000:8000 my-app
```
