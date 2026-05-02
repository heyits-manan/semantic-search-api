from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    document_id: int
    content: str

