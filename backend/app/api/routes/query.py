
from fastapi import APIRouter, HTTPException

from app.schemas.query import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    """
    Receive a user question and return an answer
    with its sources.
    """

    # Placeholder: connect this route to the RAG service later.
    raise HTTPException(
        status_code=501,
        detail="Query route is not connected yet.",
    )