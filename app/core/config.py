import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Your App"
    # Use SQLite locally, Postgres in prod (e.g., on Cloud Run / Cloud SQL)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")

    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "CHANGE_ME_IN_PROD")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    @property
    def ACCESS_TOKEN_EXPIRE_DELTA(self) -> timedelta:
        return timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)

settings = Settings()
