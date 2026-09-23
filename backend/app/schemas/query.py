
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    """Request schema for asking a question."""

    question: str = Field(
        ...,
        min_length=1,
        description="The question asked by the user",
    )


class QueryResponse(BaseModel):
    """Response schema returned by the RAG assistant."""

    answer: str
    sources: list[str] = Field(default_factory=list)