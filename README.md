# 🩺 Diabetes RAG Document Assistant

An AI-powered **Retrieval-Augmented Generation (RAG)** application designed to help people with diabetes explore and better understand their condition through educational, document-based answers.

The system retrieves relevant information from diabetes-related documents and uses a Large Language Model (LLM) to generate context-based answers while displaying the supporting sources.

> ⚠️ This project is for educational purposes only and does not replace professional medical advice.

---

## 🚀 Project Overview

The project combines:

- 📄 Diabetes-related PDF documents
- ✂️ Text extraction and chunking
- 🧠 Sentence Transformers for text embeddings
- 🔎 FAISS for semantic similarity search
- 🤖 Llama 3.2 for answer generation
- ☁️ Google Colab for running the RAG pipeline
- 🌐 ngrok for exposing the Colab API
- ⚡ FastAPI as a local API proxy
- 🎨 Streamlit as the user interface

### System Architecture

```text
Diabetes PDF Documents
        │
        ▼
   Text Extraction
        │
        ▼
      Chunking
        │
        ▼
    Embeddings
        │
        ▼
      FAISS
   Vector Database
        │
        ▼
   Retrieve Relevant
       Chunks
        │
        ▼
     Llama 3.2
        │
        ▼
   Generated Answer
        │
        ▼
   Colab FastAPI
        │
        ▼
      ngrok
        │
        ▼
 Local FastAPI Proxy
        │
        ▼
    Streamlit UI

        │
        ▼
       User

