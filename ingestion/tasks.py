from celery import shared_task
from ingestion.indexer import ingest_document
import logging

logger = logging.getLogger(__name__)

@shared_task(
    autoretry = (Exception,),
    retry_backoff = 5,
    retry_Kwargs = {"max_retries":3},
)
def ingest_document_task(filepath):
    logger.info(f"Starting ingestion for {filepath}")
    ingest_document(filepath)
    logger.info(f"Completed ingestion for {filepath}")
    