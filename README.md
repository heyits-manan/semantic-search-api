# Semantic Search API

A small FastAPI project skeleton for learning how to build a semantic search API.

This project does not implement semantic search, embeddings, document chunking, authentication, or background jobs yet.

## Project Structure

```text
semantic-search-api/
  app/
    main.py
    config.py
    db.py
    models/
      document.py
      chunk.py
    schemas/
      document.py
      search.py
    routes/
      health.py
      documents.py
      search.py
    services/
      document_service.py
      search_service.py
  alembic/
  tests/
  .env.example
  requirements.txt
  Dockerfile
  docker-compose.yml
  README.md
```

## Local Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Update `DATABASE_URL` in `.env` with your Supabase Postgres connection string.

Run the API:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/health
```

## Current Endpoints

- `GET /health`
- `POST /documents/`
- `POST /search/`

## Docker

After creating `.env`, you can run:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```
