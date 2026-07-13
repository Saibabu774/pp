from pydantic import BaseModel
from typing import Optional


class JobCreate(BaseModel):
    task_name: str
    payload: Optional[str] = None


class JobResponse(BaseModel):
    id: int
    task_name: str
    status: str

    class Config:
        from_attributes = True