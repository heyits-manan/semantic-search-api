from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title: str
    source: str | None = None


class DocumentRead(BaseModel):
    id: int
    title: str
    source: str | None = None

