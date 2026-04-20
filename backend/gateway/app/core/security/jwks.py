import time
import httpx
from core.config import settings


class JWKSCache:
    def __init__(self):
        self.keys = {}
        self.last = 0
        self.ttl = 600

    async def get(self):
        if self.keys and time.time() - self.last < self.ttl:
            return self.keys

        async with httpx.AsyncClient() as client:
            r = await client.get(settings.JWKS_URL)
            data = r.json()

        self.keys = {k["kid"]: k for k in data["keys"]}
        self.last = time.time()
        return self.keys


jwks_cache = JWKSCache()
