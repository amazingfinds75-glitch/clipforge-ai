from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import health, ingestion

app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=settings.allowed_origins,
    allow_credentials=True, allow_methods=["GET", "POST"], allow_headers=["*"])
app.include_router(health.router, prefix=settings.api_v1_prefix)
app.include_router(ingestion.router, prefix=settings.api_v1_prefix)

@app.get("/")
def root() -> dict:
    return {"name": settings.app_name, "docs": "/docs",
            "health": f"{settings.api_v1_prefix}/health"}
