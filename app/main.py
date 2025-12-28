from fastapi import FastAPI
from app.config import settings
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
@app.get("/")
def read_root():
    return {
        "message": "Welcome to E-commerce API",
        "version": settings.APP_VERSION
    }
@app.get("/health")
def health_check():
    return {"status": "healthy"}