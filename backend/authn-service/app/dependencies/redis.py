import redis.asyncio as redis
from functools import lru_cache
from core.config import settings


@lru_cache
def get_redis() -> redis.Redis:
    return redis.Redis.from_url(
        f"redis://:{settings.REDIS_PASSWORD}@wave_redis:{settings.REDIS_PORT}/0",
        decode_responses=True,
    )
