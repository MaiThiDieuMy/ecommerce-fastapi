from fastapi import FastAPI
from app.config import settings
from app.api.v1 import auth
from app.database import engine, Base
# Create tables
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
# Include routers
app.include_router(auth.router, prefix="/api/v1")
@app.get("/")
def read_root():
    return {
        "message": "Welcome to E-commerce API",
        "version": settings.APP_VERSION
    }
@app.get("/health")
def health_check():
    return {"status": "healthy"}