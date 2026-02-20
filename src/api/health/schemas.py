from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HealthResponse(BaseModel):
    status: str
    service: str
    timestamp: datetime
    version: str
    check_type: Optional[str] = None
    counting_result: Optional[dict] = None
    details: Optional[dict] = None
    


class HealthCheckRequest(BaseModel):
    service_name: Optional[str] = None
    check_type: Optional[str] = "basic"
    include_details: Optional[bool] = False
    start_number: Optional[int] = 1
    end_number: Optional[int] = 10
    step: Optional[int] = 1
