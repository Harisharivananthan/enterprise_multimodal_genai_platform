from fastapi import APIRouter
from config.settings import settings

routor = APIRouter()
@routor.get("/health")
def health_check():
    return {
        "status":"ok",
        "version":settings.APP_VERSION,
        "environment":settings.ENVIRONMENT
    }