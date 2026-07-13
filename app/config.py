from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Async Job Processing System"
    VERSION: str = "1.0.0"

    DATABASE_URL: str = "sqlite:///./jobs.db"

    MAX_RETRIES: int = 3
    WORKER_SLEEP: int = 5


settings = Settings()