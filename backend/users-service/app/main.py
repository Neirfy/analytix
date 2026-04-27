from fastapi import FastAPI
from handlers.users import router
from handlers.update import router as update


app = FastAPI(
    title="User Service",
    docs_url="/docs",
    openapi_url="/openapi.json",
)
app.include_router(router)
app.include_router(update)
