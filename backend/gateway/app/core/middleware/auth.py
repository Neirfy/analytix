from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi import Request
from jose import jwt, JWTError

from core.security.jwks import jwks_cache


class JWTMiddleware(BaseHTTPMiddleware):
    PUBLIC_PATHS = (
        # "/authn/login",
        # "/authn/register",
        "/docs",
        "/redoc",
        "/openapi.json",
        "/docs/oauth2-redirect",
    )

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):
        path = request.url.path

        if (
            path in self.PUBLIC_PATHS
            or any(path.startswith(p + "/") for p in self.PUBLIC_PATHS)
            # or path.startswith("/docs")
            # or path.startswith("/openapi.json")
            # or path.startswith("/redoc")
        ):
            return await call_next(request)

        auth = request.headers.get("Authorization")
        if not auth:
            return JSONResponse(
                status_code=401,
                content={"detail": "Missing Authorization header"},
            )

        parts = auth.split()

        if len(parts) != 2 or parts[0].lower() != "bearer":
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid Authorization format"},
            )

        token = parts[1]

        try:
            header = jwt.get_unverified_header(token)
            kid = header.get("kid")

            if not kid:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Missing kid in token"},
                )

            keys = await jwks_cache.get()

            public_key = keys.get(kid)
            if not public_key:
                jwks_cache.keys = {}
                keys = await jwks_cache.get()
                public_key = keys.get(kid)

            if not public_key:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Unknown signing key"},
                )

            payload = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],
                audience="gateway",
                issuer="authn",
            )

            request.state.user = {
                "id": payload.get("sub"),
                "roles": payload.get("roles", []),
            }

        except JWTError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid token"},
            )

        except Exception:
            return JSONResponse(
                status_code=500,
                content={"detail": "Auth middleware error"},
            )

        return await call_next(request)
