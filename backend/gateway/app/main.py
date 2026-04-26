from fastapi import FastAPI
from core.middleware.auth import JWTMiddleware

from proxy.router import proxy_router

app = FastAPI(
    title="Gateway",
    docs_url="/docs",
)

app.add_middleware(JWTMiddleware)
app.include_router(proxy_router)
