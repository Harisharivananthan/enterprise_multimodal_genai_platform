import redis
import json
from config.settings import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)


def get_cached_response(query):
    key = f"genai_cache:{query}"
    data = redis_client.get(key)

    if data:
        return json.loads(data)

    return None


def set_cached_response(query, response, ttl=3600):
    key = f"genai_cache:{query}"

    redis_client.setex(key, ttl, json.dumps(response))