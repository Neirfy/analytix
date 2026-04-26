from fastapi import APIRouter, Request, Depends

from dependencies.db import get_db
from schemas.user import LoginSchema
from schemas.token import TokenSchema

router = APIRouter(
    prefix="/authn",
    tags=["Сервис авторизации"],
)


@router.post(
    "/login",
    response_model=TokenSchema,
    description="Получение токена",
)
def login(
    data: LoginSchema,
    db=Depends(get_db),
):
    # TODO
    # user = get_user_by_id(db, user_id)
    # if not data:
    #     return {"error": "not found"}

    token: TokenSchema = TokenSchema(
        access_token="123",
        refresh_token="123",
    )

    if not token:
        return {"error": "user not found"}

    return token


@router.post(
    "/refresh",
    response_model=TokenSchema,
)
def refresh():
    # TODO
    token: TokenSchema = TokenSchema(
        access_token="123",
        refresh_token="123",
    )

    if not token:
        return {"error": "user not found"}

    return token


@router.post(
    "/validate",
    # response_model=UserOut,
)
def validate_token():
    # TODO
    valide = False
    return valide
