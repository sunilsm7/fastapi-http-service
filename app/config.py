import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # take environment variables


class Settings(BaseSettings):
    TIMEZONE: str = os.getenv('TIMEZONE', 'UTC')
    CONNECTION: str = str(os.getenv('DATABASE_CONNECTION', default="postgresql"))
    DATABASE_HOST: str = str(os.getenv('DATABASE_HOST', default="db_host"))
    DATABASE_PORT: str = str(os.getenv('DATABASE_PORT', default="5432"))
    DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME", "db_test_user")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "db_test_password")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "default_db")
    DATABASE_URL: str = os.getenv("DATABASE_URL",
                                  f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

    # Application settings
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    IS_PRODUCTION: bool = not DEBUG
    MAX_TRANSACTION_RETRIES: int = int(os.getenv("MAX_TRANSACTION_RETRIES", 2))
    RATE_LIMIT: int = 10  # requests per second
    REQUEST_DELAY: float = 1.0 / 10  # 100ms between requests
    AUTH_TEST_USERNAME: str = os.getenv("AUTH_TEST_USERNAME", "testuser")
    AUTH_TEST_PASSWORD: str = os.getenv("AUTH_TEST_PASSWORD", "testpwd")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")


settings = Settings()
