from fastapi import FastAPI
from handlers.auth import router

# from core.db import create_table

app = FastAPI(
    title="Auth Service",
    docs_url="/docs",
    # redoc_url="/docs-redoc",
    openapi_url="/openapi.json",
)
app.include_router(router)
