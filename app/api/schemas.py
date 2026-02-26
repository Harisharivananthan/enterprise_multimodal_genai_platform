from pydantic import BaseModel

def HealthResponse(BaseModel):
    status : str
    environment : str
    version : str
    