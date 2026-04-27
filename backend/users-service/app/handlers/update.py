from fastapi import APIRouter, Request, Depends
from uuid import UUID

from dependencies.db import get_db
from dependencies.service import get_user_service
from schemas.user import UpdateUserSchema, UserSchema

from service.user import UserService


router = APIRouter(
    prefix="/users/update",
    tags=["Сервис пользователя"],
)


@router.patch(
    "/username",
    response_model=UserSchema,
)
async def update_username(
    # user_id: int,
    data: UpdateUserSchema,
    service: UserService = Depends(get_user_service),
):
    user_id = UUID("c28e1131-6a70-4f6c-8480-70d1b058ef55")
    return await service.update_username(user_id, data)


# @router.post("/create", response_model=UserSchema)
# async def create_user(
#     data: CreateUserSchema,
#     service: UserService = Depends(get_user_service),
# ):
#     return await service.create_user(data)
