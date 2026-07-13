import asyncio
import random
from datetime import datetime


class JobService:

    @staticmethod
    async def process_job(job: dict):
        try:
            job["status"] = "Running"
            job["started_at"] = str(datetime.now())

            # Simulate processing time
            await asyncio.sleep(random.randint(2, 5))

            # Simulate random failure
            if random.randint(1, 10) <= 2:
                raise Exception("Simulated Job Failure")

            job["status"] = "Completed"
            job["completed_at"] = str(datetime.now())

        except Exception as e:
            job["status"] = "Failed"
            job["error_message"] = str(e)

    @staticmethod
    async def retry_job(job: dict, retry_limit: int = 3):
        while job.get("retries", 0) < retry_limit:
            await JobService.process_job(job)

            if job["status"] == "Completed":
                return

            job["retries"] += 1
            await asyncio.sleep(2)

        job["status"] = "Failed"