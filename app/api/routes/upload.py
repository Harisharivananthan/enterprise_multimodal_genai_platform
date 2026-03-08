from fastapi import APIRouter, UploadFile, File
from ingestion.tasks import ingest_document_task
import os

router = APIRouter(prefix="/upload")

DATA_DIR = "data/documents"
os.makedirs(DATA_DIR, exist_ok=True)


@router.post("/")
def upload(file: UploadFile = File(...)):
    path = os.path.join(DATA_DIR, file.filename)

    with open(path, "wb") as f:
        data = file.file.read()
        f.write(data)

    ingest_document_task.delay(path)

    return {"status": "document ingestion started"}