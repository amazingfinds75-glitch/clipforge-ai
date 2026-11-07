from fastapi import APIRouter, HTTPException
from app.schemas.ingestion import IngestionRequest, IngestionAccepted, SourceType

router = APIRouter(prefix="/ingestion", tags=["ingestion"])

@router.post("/prepare", response_model=IngestionAccepted, status_code=202)
def prepare_ingestion(request: IngestionRequest) -> IngestionAccepted:
    if request.source_type == SourceType.url and not request.url:
        raise HTTPException(status_code=422, detail="A URL is required for URL ingestion.")
    if request.source_type == SourceType.cloud_object:
        if not request.provider or not request.object_key:
            raise HTTPException(status_code=422, detail="Cloud ingestion requires provider and object_key.")
        raise HTTPException(status_code=501, detail="Cloud storage provider is not configured yet.")
    if request.source_type == SourceType.upload:
        raise HTTPException(status_code=501, detail="Upload processing is implemented in the next phase.")
    return IngestionAccepted(status="accepted_for_design",
        message="URL contract validated; secure fetching and job creation are not enabled in Phase 1.",
        source_type=request.source_type)
