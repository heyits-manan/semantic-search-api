from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/")
def upload_document():
    return {"message": "Document upload not implemented yet"}

