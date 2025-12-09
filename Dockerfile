# Stage 1: Build the Docusaurus frontend
FROM node:18 AS frontend-build
WORKDIR /app/my-book
COPY my-book/package*.json ./
RUN npm install
COPY my-book/ .
RUN npm run build

# Stage 2: Create the final image with the FastAPI backend
FROM python:3.11-slim
WORKDIR /app
COPY Backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=frontend-build /app/my-book/build /app/static
COPY Backend/ /app/
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
