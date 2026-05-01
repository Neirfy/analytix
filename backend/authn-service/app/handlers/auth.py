from fastapi import APIRouter, Depends
from fastapi import Cookie, Response

import json
from uuid import uuid4
from dependencies.db import get_db
from dependencies.redis import get_redis
from schemas.user import LoginSchema

# from schemas.token import TokenSchema

router = APIRouter(
    prefix="/authn",
    tags=["Сервис авторизации"],
)


# @router.post(
#     "/login",
#     response_model=TokenSchema,
#     description="Получение токена",
# )
# def login(
#     data: LoginSchema,
#     db=Depends(get_db),
# ):
#     # TODO
#     # user = get_user_by_id(db, user_id)
#     # if not data:
#     #     return {"error": "not found"}

#     token: TokenSchema = TokenSchema(
#         access_token="123",
#         refresh_token="123",
#     )

#     if not token:
#         return {"error": "user not found"}

#     return token


@router.post("/login")
async def login(
    data: LoginSchema,
    response: Response,
    db=Depends(get_db),
    redis=Depends(get_redis),
):
    user = await authenticate_user(db, data)

    session_id = str(uuid4())

    await redis.setex(
        f"session:{session_id}", 60 * 60 * 24, json.dumps({"user_id": str(user.id)})
    )

    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        samesite="lax",
        secure=False,
    )

    return {"ok": True}


# @router.post(
#     "/refresh",
#     response_model=TokenSchema,
# )
# def refresh():
#     # TODO
#     token: TokenSchema = TokenSchema(
#         access_token="123",
#         refresh_token="123",
#     )

#     if not token:
#         return {"error": "user not found"}

#     return token


# @router.post(
#     "/validate",
#     # response_model=UserOut,
# )
# def validate_token():
#     # TODO
#     valide = False
#     return valide


@router.post("/validate")
async def validate(
    session_id: str = Cookie(None),
    redis=Depends(get_redis),
):
    if not session_id:
        return False

    session = await redis.get(f"session:{session_id}")
    return session is not None


@router.post("/logout")
async def logout(
    response: Response,
    session_id: str = Cookie(None),
    redis=Depends(get_redis),
):
    if session_id:
        await redis.delete(f"session:{session_id}")

    response.delete_cookie("session_id")
    return {"ok": True}
