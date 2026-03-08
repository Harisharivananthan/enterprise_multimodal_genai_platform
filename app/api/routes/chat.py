from fastapi import APIRouter
from pydantic import BaseModel
import time

from app.agents.agent_orchestrator import run_agent_system
from cache.redis_cache import get_cached_response, set_cached_response
from monitoring.metrics import REQUEST_COUNT, REQUEST_LATENCY

router = APIRouter(prefix="/chat")


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(req: ChatRequest):

    query = req.question

    cached = get_cached_response(query)
    if cached:
        return {"answer": cached, "cached": True}

    REQUEST_COUNT.inc()
    start = time.time()
    answer = run_agent_system(query)
    REQUEST_LATENCY.observe(time.time() - start)
    set_cached_response(query, answer)

    return {"answer": answer, "cached": False}