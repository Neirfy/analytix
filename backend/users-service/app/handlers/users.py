from fastapi import APIRouter, Request, Depends
from uuid import UUID

from dependencies.db import get_db
from dependencies.service import get_user_service
from schemas.user import CreateUserSchema, UserSchema

from service.user import UserService


router = APIRouter(
    prefix="/users",
    tags=["Сервис пользователя"],
)


@router.get(
    "/me",
    response_model=UserSchema,
)
async def get_me(
    # user_id: int,
    service: UserService = Depends(get_user_service),
):
    user_id = UUID("c28e1131-6a70-4f6c-8480-70d1b058ef55")
    return await service.get_me(user_id)


@router.post(
    "/create",
    response_model=UserSchema,
)
async def create_user(
    data: CreateUserSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.create_user(data)


@router.delete(
    "/delete",
    response_model=UserSchema,
)
async def delete_user(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
):
    return await service.delete_user(user_id)
