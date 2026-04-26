from fastapi import APIRouter, Request
from proxy.client import forward_request

proxy_router = APIRouter()


@proxy_router.api_route(
    "/{service}/{path:path}",
    methods=["GET", "PATCH", "POST", "PUT", "DELETE"],
    include_in_schema=False,
)
async def proxy(
    service: str,
    path: str,
    request: Request,
):
    return await forward_request(service, path, request)
