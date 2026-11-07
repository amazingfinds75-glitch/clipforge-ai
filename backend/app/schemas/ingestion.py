from enum import Enum
from pydantic import BaseModel, Field, HttpUrl


class SourceType(str, Enum):
    upload = "upload"
    url = "url"
    cloud_object = "cloud_object"


class IngestionRequest(BaseModel):
    source_type: SourceType
    url: HttpUrl | None = None
    provider: str | None = Field(default=None, max_length=40)
    object_key: str | None = Field(default=None, max_length=1024)
    original_filename: str | None = Field(default=None, max_length=255)


class IngestionAccepted(BaseModel):
    status: str
    message: str
    source_type: SourceType
    job_id: str | None = None
