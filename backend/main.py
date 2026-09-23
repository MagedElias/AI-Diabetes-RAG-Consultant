
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# Load environment variables from the project root
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)


# Initialize FastAPI
app = FastAPI(
    title="RAG Document Assistant API",
    description="Local API that connects to the RAG running on Google Colab",
    version="1.0.0",
)


# Configure CORS for the Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load Colab API configuration
COLAB_API_URL = os.getenv("COLAB_API_URL", "").rstrip("/")
COLAB_API_KEY = os.getenv("COLAB_API_KEY", "")


# Request schema
class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "RAG Document Assistant API is running"
    }


# Health check endpoint
@app.get("/health")
def health():
    return {
        "status": "ok",
        "colab_configured": bool(COLAB_API_URL),
        "api_key_configured": bool(COLAB_API_KEY),
    }


# Query endpoint
@app.post("/query")
def query(request: QueryRequest):

    # Check whether the Colab API URL is configured
    if not COLAB_API_URL:
        raise HTTPException(
            status_code=503,
            detail="COLAB_API_URL is not configured",
        )

    # Add API key to request headers if configured
    headers = {}

    if COLAB_API_KEY:
        headers["X-API-Key"] = COLAB_API_KEY

    try:
        # Send the question to the Colab RAG API
        response = requests.post(
            f"{COLAB_API_URL}/ask",
            json={"question": request.question},
            headers=headers,
            timeout=180,
        )

        response.raise_for_status()

        # Return the Colab API response
        return response.json()

    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=504,
            detail="The Colab API took too long to respond",
        )

    except requests.exceptions.HTTPError as e:
        status_code = (
            e.response.status_code
            if e.response is not None
            else 502
        )

        raise HTTPException(
            status_code=502,
            detail=f"Colab API returned an error: {status_code}",
        )

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Could not connect to the Colab API",
        )