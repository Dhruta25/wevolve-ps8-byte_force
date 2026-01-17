from fastapi import FastAPI,Query
from app.api.v1.api_router import api_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}