from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class SubmissionCreate(BaseModel):
    widget_id: str = Field(..., description="ID of the widget receiving the submission")
    payload: Dict[str, Any] = Field(..., description="Form fields payload (JSON object)")

class SubmissionResponse(BaseModel):
    id: str
    widget_id: str
    payload: Dict[str, Any]
    ip_address: Optional[str] = None
    geo_data: Optional[Dict[str, Any]] = None
    created_at: datetime

    class Config:
        from_attributes = True
