from fastapi import APIRouter

router = APIRouter(prefix="/search", tags=["search"])


@router.post("/")
def search_documents():
    return {"message": "Search not implemented yet"}

