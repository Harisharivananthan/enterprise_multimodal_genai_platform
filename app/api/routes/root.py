from fastapi import APIRouter

routor = APIRouter()

@routor.get("/")
def root():
    return {
        "message":"Enterprise Multimodel Genai Platform is running"
    }