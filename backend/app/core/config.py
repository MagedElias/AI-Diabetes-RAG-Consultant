
import os
from pathlib import Path

from dotenv import load_dotenv


# Project root: ITI Final Project/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Load environment variables from the root .env file
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(ENV_FILE)


class Settings:
    """Application settings loaded from environment variables."""

    APP_NAME: str = "RAG Document Assistant API"
    APP_VERSION: str = "1.0.0"

    COLAB_API_URL: str = os.getenv("COLAB_API_URL", "").rstrip("/")
    COLAB_API_KEY: str = os.getenv("COLAB_API_KEY", "")

    REQUEST_TIMEOUT: int = 180


settings = Settings()