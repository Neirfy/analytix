import httpx


SERVICE_MAP = {
    "authn": "http://authn:8000",
    "authz": "http://authz:8000",  # TODO
    "users": "http://users:8000",  # TODO
}


async def forward_request(
    service: str,
    path: str,
    request,
):
    base_url = SERVICE_MAP.get(service)
    if not base_url:
        return {"error": "unknown service"}

    url = f"{base_url}/{path}"

    headers = dict(request.headers)

    if hasattr(request.state, "user"):
        headers["X-User-Id"] = str(request.state.user["id"])
        headers["X-Roles"] = ",".join(request.state.user["roles"])

    body = await request.body()

    async with httpx.AsyncClient() as client:
        resp = await client.request(
            method=request.method,
            url=url,
            headers=headers,
            content=body,
            params=dict(request.query_params),
        )

    return resp.json()
