from fastapi import FastAPI
from app.core.middleware.auth import JWTMiddleware

from app.proxy.router import proxy_router

app = FastAPI(title="Gateway")

app.add_middleware(JWTMiddleware)
app.include_router(proxy_router)
