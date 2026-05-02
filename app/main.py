from fastapi import FastAPI

from app.routes import documents, health, search

app = FastAPI(title="Semantic Search API")

app.include_router(health.router)
app.include_router(documents.router)
app.include_router(search.router)

