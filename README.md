# Enterprise RAG Assistant

An enterprise-grade Retrieval Augmented Generation (RAG) application built using FastAPI, Next.js, FAISS, Sentence Transformers, and Gemini.

## Features

* Multi-document upload support
* PDF parsing and chunking
* Semantic search using FAISS
* Metadata-aware retrieval
* Gemini-powered answer generation
* RAG evaluation metrics:

  * Retrieval relevance
  * Answer faithfulness
  * Response latency
* Persistent vector database
* Modern Next.js chat interface
* Source citations

## Tech Stack

### Backend

* FastAPI
* FAISS
* Sentence Transformers
* Google Gemini
* PyPDF

### Frontend

* Next.js
* TypeScript
* Tailwind CSS
* Axios

## Architecture

User Question
↓
Query Embedding
↓
FAISS Semantic Search
↓
Relevant Document Chunks
↓
Gemini LLM
↓
Final Answer + Sources + Evaluation

## Running Locally

### Backend

```
cd backend
uvicorn app:app --reload
```

Runs on:

http://localhost:8000

### Frontend

```
cd frontend
npm run dev
```

Runs on:

http://localhost:3000

## Future Improvements

* Hybrid Search (BM25 + FAISS)
* Cross Encoder Re-ranking
* JWT Authentication
* Role Based Access Control
* Streaming Responses
* Analytics Dashboard
* Cloud Deployment
