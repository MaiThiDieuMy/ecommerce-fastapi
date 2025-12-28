from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME: str = "E-commerce FastAPI"
    APP_VERSION: str = "0.1.0"
    DATABASE_URL: str = "sqlite:///./ecommerce.db"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    
    class Config:
        env_file = ".env"
settings = Settings()