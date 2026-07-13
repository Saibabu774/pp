from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
from uuid import uuid4

router = APIRouter()

# Temporary in-memory storage
jobs = []


class JobCreate(BaseModel):
    job_type: str
    payload: Dict[str, Any]
    priority: str = "medium"


@router.post("/")
def create_job(job: JobCreate):
    job_data = {
        "id": str(uuid4()),
        "job_type": job.job_type,
        "payload": job.payload,
        "priority": job.priority,
        "status": "Pending",
        "retries": 0
    }

    jobs.append(job_data)

    return {
        "message": "Job submitted successfully",
        "job": job_data
    }


@router.get("/")
def get_jobs():
    return jobs


@router.get("/{job_id}")
def get_job(job_id: str):
    for job in jobs:
        if job["id"] == job_id:
            return job
    raise HTTPException(status_code=404, detail="Job not found")


@router.delete("/{job_id}")
def delete_job(job_id: str):
    for job in jobs:
        if job["id"] == job_id:
            jobs.remove(job)
            return {"message": "Job deleted successfully"}

    raise HTTPException(status_code=404, detail="Job not found")