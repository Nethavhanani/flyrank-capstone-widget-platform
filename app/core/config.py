from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FlyRank Widget Platform"
    PORT: int = 3000
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/widget_db"
    GEO_PROVIDER_A_URL: str = "http://ip-api.com/json/"
    GEO_PROVIDER_B_URL: str = "https://ipapi.co/"

    class Config:
        env_file = ".env"

settings = Settings()
