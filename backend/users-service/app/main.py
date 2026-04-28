from fastapi import FastAPI
from handlers.router import router


app = FastAPI(
    title="User Service",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.include_router(router)
