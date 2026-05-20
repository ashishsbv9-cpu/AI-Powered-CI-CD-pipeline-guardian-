from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Any

class FailureBase(BaseModel):
    error_log: str
    pipeline_id: str

class FailureCreate(FailureBase):
    repository: str
    branch: str

class FailureResponse(FailureBase):
    id: int
    repository: str
    branch: str
    created_at: datetime
    root_cause: Optional[str] = None
    ai_analysis: Optional[Any] = None

    class Config:
        from_attributes = True

class PipelineFailureHistory(BaseModel):
    id: int
    pipeline_id: int
    error_log: str
    created_at: datetime
    root_cause: Optional[str] = None
    ai_analysis: Optional[Any] = None

    class Config:
        from_attributes = True

class PipelineHistory(BaseModel):
    id: int
    repository: str
    branch: str
    status: str
    created_at: datetime
    failures: List[PipelineFailureHistory] = []

    class Config:
        from_attributes = True

