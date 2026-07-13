import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("async_job_system")


def log_job_created(job_id: str):
    logger.info(f"Job Created | ID={job_id}")


def log_job_started(job_id: str):
    logger.info(f"Job Started | ID={job_id}")


def log_job_completed(job_id: str):
    logger.info(f"Job Completed | ID={job_id}")


def log_job_failed(job_id: str, error: str):
    logger.error(f"Job Failed | ID={job_id} | Error={error}")


def log_job_retry(job_id: str, attempt: int):
    logger.warning(f"Retry Attempt {attempt} | Job ID={job_id}")