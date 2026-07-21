from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class IncidentCreate(BaseModel):
    log_text: str


class IncidentResponse(BaseModel):
    id: int
    severity: str
    threat_type: str
    mitre_technique: Optional[str] = None
    summary: str
    created_at: datetime

    class Config:
        from_attributes = True
