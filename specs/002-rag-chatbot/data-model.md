# Data Model

This document outlines the data models for the RAG chatbot feature.

## Conversation

Represents a user's interaction with the chatbot.

- **id**: `UUID` (Primary Key)
- **created_at**: `Timestamp`
- **updated_at**: `Timestamp`

## Message

A single query from a user or a response from the chatbot.

- **id**: `UUID` (Primary Key)
- **conversation_id**: `UUID` (Foreign Key to Conversation)
- **role**: `String` ("user" or "assistant")
- **content**: `Text`
- **created_at**: `Timestamp`

## Document

A chunk of text from the book's content that is indexed and used for retrieval.

- **id**: `UUID` (Primary Key)
- **source**: `String` (e.g., file path or URL)
- **content**: `Text`
- **embedding**: `Vector`
- **created_at**: `Timestamp`

## IngestionLog

A record of a content ingestion event.

- **id**: `UUID` (Primary Key)
- **job_id**: `String`
- **status**: `String` ("pending", "running", "completed", "failed")
- **files_processed**: `Integer`
- **created_at**: `Timestamp`
- **completed_at**: `Timestamp`
