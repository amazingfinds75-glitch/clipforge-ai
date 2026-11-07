from fastapi import APIRouter
from app.services.providers import LocalProcessingProvider, CloudProcessingProvider

router = APIRouter(tags=["system"])

@router.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "clipforge-api"}

@router.get("/capabilities")
def capabilities() -> dict:
    return {"processing": [LocalProcessingProvider().status().__dict__, CloudProcessingProvider().status().__dict__],
            "ingestion": ["upload", "url", "cloud_object"]}
