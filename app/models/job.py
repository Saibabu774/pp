from sqlalchemy import Column, Integer, String, JSON, DateTime
from datetime import datetime

from database.database import Base


class Job(Base):
    _tablename_ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    priority = Column(String, default="medium")
    status = Column(String, default="Pending")
    retries = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    error_message = Column(String, nullable=True)