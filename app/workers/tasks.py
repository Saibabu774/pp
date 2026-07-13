import time
import random

from app.queue.celery_app import celery


@celery.task(bind=True, max_retries=3)
def process_job(self, job_id, job_type, payload):
    try:
        print(f"Processing Job: {job_id}")
        print(f"Job Type: {job_type}")
        print(f"Payload: {payload}")

        # Simulate processing time
        time.sleep(random.randint(3, 8))

        # Simulate random failure (20% chance)
        if random.randint(1, 10) <= 2:
            raise Exception("Simulated processing failure")

        return {
            "job_id": job_id,
            "status": "Completed",
            "message": "Job processed successfully"
        }

    except Exception as exc:
        print(f"Job Failed: {exc}")

        raise self.retry(exc=exc, countdown=5)